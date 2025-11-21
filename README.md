# Machine-Learning

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)
![Dataset](https://img.shields.io/badge/dataset-Kaggle-orange)

This repository presents several types of machine learning (ML) algorithms. The idea is to provide an overview of how to use these algorithms and how to validate their results.  
 
I have tried to explain them as clearly as possible, including examples and some mathematical theory to help understand the behavior of the algorithms I used. I am aware that many aspects could be explained in greater detail, but my intention here is simply to share the knowledge I have gained as a beginner.  
 
Happy exploring, everyone!

## General structure of the repo

```text
├── name_models           # functions usefull for models
│   ├── __init__.py
│   ├── preprocess.py
│   └── utils.py
├── database
│   ├── models
│   │   └── name_model.pkl # model saved as pickle
│   └── name_file.csv      # csv with the data
├── examples
│   └── notebooks          # notebooks
├── poetry.lock
├── pyproject.toml         # list of dependencies
├── LICENSE                # license file
└── README.md              # documentation
```


## Setting the environment

For this project, I choose to use ``poetry`` as a package manager. To do this, you can follow the following steps:

1. In your python environment (or virtual env):
```bash
pip install poetry
```

2. Then download all the dependencies:
```bash
poetry install
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you’d like to help improve the quality of this project.  