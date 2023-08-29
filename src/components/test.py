import sys
from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion

obj = DataIngestion()
train_path, test_path = obj.initiate_data_ingestion()

data_transformation = DataTransformation()
train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_path, test_path)