import os
import zipfile
from urllib.request import urlretrieve
from src.datascience import logger
from src.datascience.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info:\n{headers}")

        else:
            file_size = os.path.getsize(self.config.local_data_file) / (1024 * 1024)  # Convert bytes to MB
            logger.info(f"File already exists with size: {file_size:.2f} MB")

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted files to {unzip_path}")

