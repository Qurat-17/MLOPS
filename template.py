import os
from pathlib import Path
import logging

#folder
print(Path("a/b/c.txt"))

list_of_files = [

".github/workflows/.keepgit",
"src/__init__.py",
"src/components/__init__.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/exception/exception.py",
"src/logger/logging.py",
"src/utils/__init__.py",
"src/utils/utils.py",
"src/pipeline/__init__.py",
"src/pipeline/traning.py",
"src/pipeline/prediction.py",
"tests/unit/__init__.py",
"tests/integration/__init__.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.ini",
"experiment/experiments.ipynb",
"templates/index.html"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file:{filename}")
    if(not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty fiel:{filepath}")

    else :
        logging.info(f"{filename}is already exists")