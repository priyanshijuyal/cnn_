# Plant Disease Detection Using Convolutional Neural Networks (CNN)

## Overview

Welcome to the Plant Disease Detection project repository! This project aims to develop an efficient and accurate system for detecting diseases in plants using Convolutional Neural Networks (CNN). The implementation is based on deep learning techniques, specifically designed to analyze images of plant leaves and identify potential diseases.


## Introduction

Plant diseases can have a significant impact on crop yield and quality. Early detection of these diseases is crucial for effective plant disease management. This project utilizes CNNs, a class of deep neural networks, to automatically identify and classify diseases in plant leaves.

## Features

- **Image Classification:** The model classifies plant images into different disease categories.
- **User-friendly Interface:** A simple and intuitive interface for users to interact with the model.
- **Scalability:** The model can be easily scaled to handle large datasets and diverse plant species.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.x
- TensorFlow
- Keras
- NumPy
- Matplotlib
- OpenCV

## Installation

1. Clone the repository:

```bash
git clone https://github.com/priyanshijuyal/cnn_.git
cd plant-disease-detection
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the plant disease detection system:

1. Prepare your plant images or use the provided sample images.
2. Run the detection script:

```bash
python detect_disease.py --image_path /path/to/your/image.jpg
```

## Dataset

The dataset used for training and testing the model is available at kaggle datasets download -d abdallahalidev/plantvillage-dataset. You can download and use it for your experiments.

## Model Training

To train the model on your custom dataset, follow these steps:

1. Prepare your dataset with labeled images.
2. Configure the dataset path and parameters in the `train_model.py` script.
3. Run the training script:

```bash
python train_model.py
```

## Evaluation

Evaluate the model's performance using the evaluation script:

```bash
python evaluate_model.py
```

## Results

Detailed results and metrics obtained from model evaluation will be displayed, providing insights into the model's accuracy and performance.

## Contributing

Contributions are welcome! Please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your purposes.

---

Feel free to reach out if you have any questions or issues. Happy coding!
