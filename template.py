import os
from pathlib import Path

project_name = 'src'

listOfFiles = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml"
]


for filePath in listOfFiles:  # Looping through file paths
    filePath = Path(filePath) # converting to 'Path' object
    fileDir, fileName = os.path.split(filePath) # splitting into directory and filename
    if fileDir != "": # creating directories if they don't exist
        os.makedirs(fileDir, exist_ok=True)
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0): # creating file if not present or empty
        with open(filePath, "w") as f:
            pass
    else: # printing meg if already exists
        print(f"File is already present at: {filePath}")

        # username :- shreyankkasabale
        # password :- av095TkFfzkaqBKg
        # mongodb+srv://shreyankkasabale:<db_password>@cluster0.vzbcjhd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0