from src.datascience import logger

from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evalution_pipeline import ModelEvaluationTrainingPipeline

logger.info("Welcome to our Custom logging Data Science")

STAGE_NAME="DATA INGESTION STAGE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<< ")
    obj= DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>> stage{STAGE_NAME} completed<<<<<<<< ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<< ")
    obj= DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>> stage{STAGE_NAME} completed<<<<<<<< ")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<< ")
    obj= DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>> stage{STAGE_NAME} completed<<<<<<<< ")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= 'Model Trainer stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<< ")
    obj= ModelTrainerTrainingPipeline()
    obj.initaite_model_training()
    logger.info(f">>>>> stage{STAGE_NAME} completed<<<<<<<< ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


