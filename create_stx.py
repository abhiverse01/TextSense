import os

# Define subdirectories to create within the current directory (TextSense)
dirs = [
    'data/raw',
    'data/processed',
    'models/distilbert_finetuned',
    'scripts',
    'notebooks',
    'results/generated_text',
    'results/training_logs'
]

# Create subdirectories
for dir_path in dirs:
    os.makedirs(dir_path, exist_ok=True)

# Define initial files to create within the current directory (TextSense)
files = [
    '.gitignore',
    'README.md',
    'requirements.txt',
    'scripts/preprocess.py',
    'scripts/train.py',
    'scripts/generate.py',
    'notebooks/exploration.ipynb'
]

# Create empty files
for file_path in files:
    with open(file_path, 'w') as f:
        pass  # Just create an empty file

print("Subfolders and files created in the current directory.")
