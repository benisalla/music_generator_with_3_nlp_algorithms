<div align="center">
  <img src="https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/1cb68f56-61c5-4540-b934-3562d2f15a42" width="200" height="200"/>
  <h1>MGTLR: Music Generator using Transformer, LSTM, and RNN</h1>
  <p>Implementing a Music Generation model using Transformer, LSTM, and RNN from scratch.</p>
</div>

---

## Table of Contents 📘
- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Training](#training)
- [Fine-Tuning](#fine-tuning)
- [Some Examples](#model-performance)
- [License](#license)
- [About Me](#about-me)

---

## About The Project

<div align="center">
  <img src="https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/a3eed552-ff00-4cd0-920a-9bd02175ba9e" width="600" height="300"/>
</div>



MGTLR offers a minimalist, yet complete implementation of music generation using Transformer, LSTM, and RNN architectures. This project aims to provide a clear and structured approach to building neural networks for music generation, making it accessible for educational purposes and practical applications alike.

---

## Features

- **Modular Design**: Clear separation of components like data processing, model architecture, and training scripts.
- **Customizable**: Easy to adapt the architecture and data pipeline for various datasets and applications.
- **Poetry Dependency Management**: Utilizes Poetry for simple and reliable package management.

---

## Project Structure
```
MGTLR
│
├── generated_songs           # Generated music files
├── music_generator           # Main project directory
│   ├── app                   # Application files
│   ├── core                  # Core configurations and caching
│   ├── data                  # Data processing modules
│   ├── model                 # Model components
│   └── src                   # Source files
│       ├── checkpoints       # Model checkpoints
│       ├── dataset           # Dataset handling
│       └── tokenizer         # Tokenizer modules
├── tests                     # Test scripts
│   ├── model                 # Model tests
│   └── tokenizer             # Tokenizer tests
├── tokenizing                # Tokenizing scripts
│   └── tokenizer             # Tokenizer implementation
│       ├── __init__.py       # Initializer for tokenizer
│       ├── KerasTokenizer.py # Keras Tokenizer implementation
│       ├── MGTokenizer.py    # MG Tokenizer implementation
│       ├── NaiveTokenizer.py # Naive Tokenizer implementation
│       ├── train_keras_tokenizer.py # Script to train Keras tokenizer
│       └── train_mg_tokenizer.py    # Script to train MG tokenizer
├── finetune.py               # Script for fine-tuning the model
├── train.py                  # Script to train the model
├── .gitignore                # Git ignore file
└── README.md                 # Project README file

```

---

## Built With
This section lists the major frameworks/libraries used to bootstrap your project:
- [PyTorch](https://pytorch.org/)

---

## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/benisalla/mg-transformer.git
   ```
2. Install Poetry packages
   ```sh
   poetry install
   ```

---

## Usage

How you can use this code:

### Training

To train the model using the default configuration:

```bash
poetry run python train.py
```

### Fine-Tuning

To fine-tune a pre-trained model:

```bash
poetry run python finetune.py
```

---

### Examples of Songs Generated

Here are some examples of songs generated by the MGTLR model:



!audio[ title ]( https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/b6117374-eb42-4e68-9e8a-dc05da1fbc98 ){ size: 10, duration: 10, cycle: forever }




https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/cdc9c03f-4a22-4776-98ae-71d532800ff6



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/93f4042f-d17a-4382-8d0a-7e54632d321c



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/ae2c34ea-89cc-4bc8-aaf5-88d92422a8d1



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/f1cb56e8-1963-4234-9087-fff7cb875333



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/3c882167-ec4a-4f57-811f-1725255e4da7



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/f1eeb63e-0b8e-45db-b26e-0ddb39ad65d6



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/f2175c77-c903-415c-be10-69fd5248ed65



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/0001222a-20cf-4f1b-85b5-d06d77c7398e



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/338f7ff4-f0e6-47fd-a5b4-55ec13e28736



https://github.com/benisalla/music_generator_with_3_nlp_algorithms/assets/89405673/eeccf4e8-d8a2-45f9-9cfe-bec4bf6bfbcf










---

## License

This project is made available under **fair use guidelines**. While there is no formal license associated with the repository, users are encouraged to credit the source if they utilize or adapt the code in their work. This approach promotes ethical practices and contributions to the open-source community. For citation purposes, please use the following:

```bibtex
@misc{mg_transformer_2024,
  title={MGTLR: Music Generator using Transformer, LSTM, and RNN},
  author={Ben Alla Ismail},
  year={2024},
  url={https://github.com/benisalla/mg-transformer}
}
```

---

## About Me

🎓 **Ismail Ben Alla** - Neural Network Enthusiast

I am deeply passionate about exploring artificial intelligence and its potential to solve complex problems and unravel the mysteries of our universe. My academic and professional journey is characterized by a commitment to learning and innovation in AI, deep learning, and machine learning.

### What Drives Me
- **Passion for AI**: Eager to push the boundaries of technology and discover new possibilities.
- **Continuous Learning**: Committed to staying informed and skilled in the latest advancements.
- **Optimism and Dedication**: Motivated by the challenges and opportunities that the future of AI holds.

I thoroughly enjoy what I do and am excited about the future of AI and machine learning. Let's connect and explore the endless possibilities of artificial intelligence together!

<div align="center">
  <a href="https://twitter.com/ismail_ben_alla" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="ismail_ben_alla" height="30" width="40" />
  </a>
  <a href="https://linkedin.com/in/ismail-ben-alla-7144b5221/" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="ismail-ben-alla-7144b5221/" height="30" width="40" />
  </a>
  <a href="https://instagram.com/ismail_ben_alla" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="ismail_ben_alla" height="30" width="40" />
  </a>
</div>

---

<div align="center">
  <h4>Get ready to see music transform into a symphony 🎵✨🎶</h4>
  <img src="https://github.com/benisalla/Tiny-ViT-Transformer-from-scratch/assets/89405673/087e0049-d113-4df6-8fb3-183ebc4f85e1" width="500" height="300"/>
</div>
