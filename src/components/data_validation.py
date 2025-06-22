import json
import os
import sys

import pandas as pd
from pandas import DataFrame

from src.exception import MyException
from src.logger import logging
from src.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from src.utils.main_utils import read_yaml_file
from src.entity.config_entity import DataValidationConfig
from src.constants import SCHEMA_FILE_PATH


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):

        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self.schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e, sys)


    def validation_number_of_columns(self, dataframe: DataFrame) -> bool:

        try:
            noOfCurrentDataFrameColumns = len(dataframe.columns)
            noOfExpectedDataFrameColumns = len(self.schema_config['columns'])
            status = noOfCurrentDataFrameColumns == noOfExpectedDataFrameColumns
            logging.info(f"I required column present? - [{status}]")
            return status
        except Exception as e:
            raise MyException(e, sys)


    def is_columns_exist(self, dataframe: DataFrame) -> bool:

        try:
            dataframeColumns = dataframe.columns
            missingNumericalColumns = []
            missingCategoricalColumns = []

            for column in self.schema_config["numerical_columns"]:

                if column not in dataframeColumns:
                    missingNumericalColumns.append(column)

            for column in self.schema_config['categorical_columns']:

                if column not in dataframeColumns:
                    missingCategoricalColumns.append(column)


            if len(missingNumericalColumns) > 0:
                logging.info(f"Missing numerical column: [{missingNumericalColumns}]")

            if len(missingCategoricalColumns) > 0:
                logging.info(f"Missing categorical column: [{missingCategoricalColumns}]")


            return False if len(missingCategoricalColumns) > 0 or len(missingNumericalColumns) > 0 else True

        except Exception as e:
            raise MyException(e, sys)


    @staticmethod
    def read_data(file_path) -> DataFrame:

        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e, sys)


    def initiate_data_validation(self) -> DataValidationArtifact:

        try:
            validation_error_message = ""
            logging.info("Starting data Validation")

            train_df = DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path)
            test_df = DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path)

            # checking col len of Dataframe for train/test df
            trainStatus = self.validation_number_of_columns(dataframe=train_df)
            if not trainStatus:
                validation_error_message += f"Columns are missing in training dataframe"
            else:
                logging.info(f"All required columns present in training dataframe? - [{trainStatus}]")

            testStatus = self.validation_number_of_columns(dataframe=test_df)
            if not testStatus:
                validation_error_message += f"Columns are missing in training dataframe"
            else:
                logging.info(f"All required columns present in testing dataframe? - [{testStatus}]")

            # Validating col dtype for train/test df
            trainStatus = self.is_columns_exist(dataframe=train_df)

            if not trainStatus:
                validation_error_message += f"Columns datatype mismatch in training dataframe."
            else:
                logging.info(f"Do all columns have expected datatype in training dataframe? - [{trainStatus}]")

            testStatus = self.is_columns_exist(dataframe=test_df)
            if not testStatus:
                validation_error_message += f"Columns datatype mismatch in testing dataframe."
            else:
                logging.info(f"Do all columns have expected datatype in testing dataframe? - [{trainStatus}]")

            validation_status = len(validation_error_message) == 0

            data_validation_artifact = DataValidationArtifact(
                validation_status = validation_status,
                message= validation_error_message,
                validation_report_file_path=self.data_validation_config.validation_report_file_path
            )

            # Ensure the directory for validation_report_file_path exists
            report_dir = os.path.dirname(self.data_validation_config.validation_report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            # Save validation status and message to a JSON file
            validation_report = {
                "Validation_status": validation_status,
                "Message": validation_error_message.strip()
            }

            with open(self.data_validation_config.validation_report_file_path, "w") as report_file:
                json.dump(validation_report, report_file, indent=4)

                logging.info("Data validation artifact created and saved to JSON file.")
                logging.info(f"Data validation artifact: {data_validation_artifact}")

            return data_validation_artifact

        except Exception as e:
            raise MyException(e, sys)
