import sys
from pathlib import Path
# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from config import settings



# Set Kaggle environment variables
os.environ['KAGGLE_USERNAME'] = settings.KAGGLE_USERNAME
os.environ['KAGGLE_KEY'] = settings.KAGGLE_KEY.get_secret_value()

# Define the target directory for downloading the dataset
download_dir = Path(__file__).resolve().parent

# Run the Kaggle command to download the dataset into the data/ folder
os.system(f"kaggle competitions download -c h-and-m-personalized-fashion-recommendations -p {download_dir}")

for zip_file in download_dir.glob("*.zip"):
    print(f"Unzipping {zip_file}...")
    os.system(f'tar -xf "{zip_file}" -C "{download_dir}"') 




