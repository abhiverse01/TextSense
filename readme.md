# TextSense

TextSense is a neural network-based text generation project that leverages the DistilBERT model to generate long-range, naturally varying texts. The model is trained on a large dataset of research papers to ensure detailed and human-like academic writing. The project aims to produce coherent, varied, and indistinguishable from human-written content, making it resilient against AI text detectors.

## Features

- **Model Base**: Utilizes the open-source DistilBERT base uncased model.
- **Dataset**: Trained on a comprehensive collection of research papers (e.g., arXiv, PubMed).
- **Text Generation**: Capable of generating long-form, detailed, and varied academic texts.
- **Human-Like Writing**: Designed to mimic human writing styles to evade AI detection tools.

## Project Structure

```
TextSense/
│
├── data/
│   ├── raw/                         # Raw research paper datasets
│   └── processed/                   # Preprocessed datasets after tokenization
│
├── models/
│   └── distilbert_finetuned/        # Fine-tuned DistilBERT model checkpoints
│
├── scripts/
│   ├── preprocess.py                # Script to preprocess datasets
│   ├── train.py                     # Script to fine-tune the model
│   └── generate.py                  # Script to generate long-range text using the model
│
├── notebooks/
│   └── exploration.ipynb            # Jupyter notebook for experimentation and exploration
│
├── results/
│   ├── generated_text/              # Generated text files for evaluation
│   └── training_logs/               # Training logs and model evaluation results
│
├── .gitignore                       # To ignore unwanted files (e.g., checkpoints, large datasets)
├── README.md                        # Project documentation
└── requirements.txt                 # Dependencies and libraries
```

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/TextSense.git
   cd TextSense
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Dataset:**
   - Place your raw research paper datasets in the `data/raw/` directory.
   - Run the preprocessing script:
     ```bash
     python scripts/preprocess.py
     ```

4. **Train the Model:**
   ```bash
   python scripts/train.py
   ```

5. **Generate Text:**
   ```bash
   python scripts/generate.py
   ```

## Usage

- **Preprocessing Data:**
  The `preprocess.py` script handles cleaning and tokenizing the raw datasets to prepare them for training.

- **Training the Model:**
  The `train.py` script fine-tunes the DistilBERT model using the processed dataset. It saves checkpoints in the `models/distilbert_finetuned/` directory.

- **Generating Text:**
  The `generate.py` script uses the fine-tuned model to generate long-range, human-like text based on input prompts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Google Colab](https://colab.research.google.com/)
- [arXiv Dataset](https://arxiv.org/help/bulk_data)



