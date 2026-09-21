import pydicom
import cv2
import numpy as np
import os

SOURCE_DIR = r'C:\AngioProject\Old_Data'
TARGET_DIR = r'C:\AngioProject\AI_Framing_Data'

def get_frame_score(frame):
    # convert to 8 bit
    frame_8bit = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # 1. edges
    edges = cv2.Canny(frame_8bit, 50, 150)
    edge_score = np.sum(edges)

    # 2. contrast (variance)
    contrast_score = np.var(frame_8bit)

    # score 
    total_score = edge_score * 0.7 + contrast_score * 0.3

    return total_score, frame_8bit


def process_mirror_organization(top_k=10):
    print("🚀 Smart Filtering Started...")

    clahe = cv2.createCLAHE(clipLimit=1.2, tileGridSize=(8, 8))

    for root, dirs, files in os.walk(SOURCE_DIR):
        dcm_files = [f for f in files if not f.startswith('.')]

        if dcm_files:
            relative_path = os.path.relpath(root, SOURCE_DIR)
            new_root_path = os.path.join(TARGET_DIR, relative_path)
            os.makedirs(new_root_path, exist_ok=True)

            for file in dcm_files:
                try:
                    ds = pydicom.dcmread(os.path.join(root, file))
                    pixels = ds.pixel_array

                    if len(pixels.shape) < 3:
                        continue

                    scored_frames = []

                    # each frame score calculation
                    for idx in range(len(pixels)):
                        frame = pixels[idx]
                        score, frame_8bit = get_frame_score(frame)
                        scored_frames.append((score, frame_8bit, idx))

                    
                    scored_frames.sort(reverse=True, key=lambda x: x[0])
                    best_frames = scored_frames[:top_k]

                    
                    for i, (score, frame_8bit, idx) in enumerate(best_frames):
                        enhanced = clahe.apply(frame_8bit)
                        final_frame = cv2.GaussianBlur(enhanced, (3, 3), 0)

                        img_name = f"{file}best{i:02d}.png"
                        cv2.imwrite(os.path.join(new_root_path, img_name), final_frame)

                    print(f"✅ Done: {relative_path} -> {file}")

                except Exception as e:
                    print(f"❌ Error in {file}: {e}")

    print("\n✨ Finished! Best 10 frames selected per video.")


if _name_ == "_main_":
    process_mirror_organization(top_k=10)
