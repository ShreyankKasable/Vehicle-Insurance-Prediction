import os
from datetime import date

# CONSTANTS RELATED TO MONGO-DB CONNECTION
DATABASE_NAME = "VehicleInsurancePrediction"
COLLECTION_NAME = "Vehicle-Insurance-Prediction-Data"
MONGO_DB_URL_KEY = "MONGODB_URL"



# CONSTANT RELATED TO PIPELINE
PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "Response"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

# DATASET RELATED CONSTANTS
FILE_NAME: str = "data.csv"
TRAIN_DATA_FILE_NAME: str = "train.csv"
TEST_DATA_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# AWS RELATED CONSTANTS
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


# COMPONENT RELATED CONSTANTS :-

# ================================
# DATA INGESTION RELATED CONSTANTS
# ================================
DATA_INGESTION_COLLECTION_NAME: str = "Vehicle-Insurance-Prediction-Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

# =================================
# DATA VALIDATION RELATED CONSTANTS
# =================================
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# =====================================
# DATA TRANSFORMATION RELATED CONSTANTS
# =====================================
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# ===============================
# MODEL TRAINER RELATED CONSTANTS
# ===============================
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS = 200
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 6
MIN_SAMPLE_SPLIT_MAX_DEPTH: int = 10
MIN_SAMPLE_SPLIT_CRITERION: str = "entropy"
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101

# ==================================
# MODEL EVALUATION RELATED CONSTANTS
# ==================================
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "vehicle-insurance-prediction-mlops"
MODEL_PUSHER_S3_KEY = "model-registry"

APP_HOST = "0.0.0.0"
APP_PORT = 5000

