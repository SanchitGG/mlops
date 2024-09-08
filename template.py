import os
from pathlib import Path
list_of_files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_train.py",
    "src/components/model_eval.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "src/utils/util.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirement.txt",
    "requirement_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "exp/experiment.ipynb"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent  # get the directory part of the path
    if not filedir.exists():
        os.makedirs(filedir, exist_ok=True)  # create directories if they don't exist
        
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch() 
