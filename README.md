# Art Classification: Real vs AI-Generated using VGG19

## Overview

-  This repository contains a project aimed at classifying artworks using the VGG19 deep learning model. The project leverages the power of convolutional neural networks (CNNs) to identify and categorize various styles and genres of art.
-  The VGG19 model, known for its depth and powerful feature extraction capabilities, is employed to achieve high accuracy in art classification tasks.

---

## About Dataset

-  The dataset is a captivating ensemble of images sourced from two distinct channels: web scraping and AI-generated content. The content covers many subjects; however, special emphasis was placed on these topics: people, animals, portraits, scenery, and psychedelics.
-  These images are harvested from various online sources across the web. Ranging from landscapes, paintings, psychedelic trips, and portraits, the web-scraped images offer a glimpse into the vast spectrum of digital imagery available online.

---

## Features

  -  **VGG19 Model**: Utilizes the VGG19 architecture pre-trained on ImageNet, adapted for the specific task of distinguishing real art from AI-generated art.Image Preprocessing: Implements techniques such as resizing, normalization, and data augmentation to improve model accuracy and robustness.
  -  **Transfer Learning**: Applies transfer learning to fine-tune the pre-trained VGG19 model on the custom dataset.
  -  **Binary Classification**: Classifies images into two categories: Real Art and AI-Generated Art.
  -  **Evaluation**: Includes performance metrics such as accuracy, precision, recall, and F1-score for comprehensive model evaluation.
  -  **Visualization**: Provides tools for visualizing model predictions and understanding feature extraction.

---

## Acknowledgments
  -  The VGG19 model architecture was developed by the **Visual Geometry Group at Oxford**.
  -  The project utilizes TensorFlow and Keras for deep learning implementation.
  -  The dataset used in this project was built by [**Cash Bowman**](https://www.kaggle.com/cashbowman/) in kaggle.


