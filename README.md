# AngioLens Data Code

## Overview

This repository contains the code used to generate and technically validate the AngioLens coronary angiography dataset.

The repository is organized into three main components:

1. Dataset generation and preprocessing
2. Coronary vessel segmentation training
3. Final segmentation evaluation

## 1. Dataset Generation and Preprocessing

### `AngioLens_Data_Preprocessing.py`

This script processes multi-frame DICOM coronary angiography videos and generates the final image dataset.

**Main functionalities:**

- DICOM frame extraction and normalization
- Edge- and contrast-based frame scoring
- Automated selection of informative frames
- CLAHE-based image enhancement
- Gaussian noise reduction
- Preservation of the original folder structure
- PNG image generation

## 2. Coronary Vessel Segmentation Training

### `AngioLens_Vessel_Training.ipynb`

This notebook implements the segmentation-based technical validation and model training pipeline.

**Main functionalities:**

- Dual-model FR-UNet inference
- Consensus pseudo-label generation
- Pseudo-label quality assessment and filtering
- Patient-level dataset splitting
- Data augmentation
- FR-UNet fine-tuning
- Training and validation monitoring

## 3. Final Segmentation Evaluation

### `AngioLens_FRUNet_Final_Evaluation.ipynb`

This notebook performs the final evaluation of the fine-tuned FR-UNet model.

**Main functionalities:**

- Validation-based threshold optimization
- Independent test-set evaluation
- Bootstrap confidence intervals
- Category-wise performance analysis
- Advanced segmentation metrics
- Failure analysis
- Qualitative evaluation

## Dataset

The AngioLens dataset is publicly available on Zenodo.

**DOI:** 10.5281/zenodo.20813162

## Citation

If you use AngioLens or the accompanying code in your research, please cite the associated Data Descriptor.
