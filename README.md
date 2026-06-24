Overview
This repository contains the official implementation used to generate the AngioLens coronary angiography dataset and train deep learning models for coronary vessel segmentation.

The repository is organized into two main components:

Dataset Generation and Preprocessing
Coronary Vessel Segmentation Training

00_dataset_generation.py

Automated preprocessing pipeline for coronary angiography dataset generation.

Main functionalities:

Reading multi-frame DICOM angiography videos.
Frame normalization using min-max normalization.
Edge information extraction using the Canny edge detector.
Contrast assessment using intensity variance.
Frame quality scoring and ranking.
Selection of the most informative frames from each angiography video.
Image enhancement using CLAHE.
Noise reduction using Gaussian filtering.
Preservation of the original folder hierarchy.
Export of selected frames as 512 × 512 PNG images.

This pipeline converts raw clinical angiography videos into a structured AI-ready image dataset while reducing redundancy and preserving diagnostically relevant information.

01_vessel_training.py

Coronary vessel segmentation training pipeline.

Main functionalities:

U-Net architecture with ResNet34 encoder.
Training using manually annotated vessel masks.
Data augmentation using Albumentations.
Combined Dice and Binary Cross-Entropy loss.
Vessel mask prediction and refinement.
Coronary artery centerline extraction.
Visualization and evaluation of segmentation results.
