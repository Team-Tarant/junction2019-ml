# Seikkai.ly ML

Machine learning model & Python micro-service for estimating the visitor count at Nuuksio. Data is counter data from (https://www.dropbox.com/sh/4yz0jq2795cnwt7/AACaT8As6jL3q973FpFgNnIaa?dl=0)

### Development

Requires python 3.7 and Poetry.

  poetry install

  poetry run flask run


### Finetuning the ML model

  poetry run jupyter-notebook

### Usage

API endpoint: /predict

| Parameter     | Required | Explanation                                                           | Example    |
|:------------- |:---------|:----------------------------------------------------------------------|:-----------|
| timestamp     | Yes      | Time to predict, in Unix format                                       | 1563634800 |
| counterId     | No       | Counter id in the park. If not specified, predicts for the whole park | 151989     |

Example request:

  http://127.0.0.1:5000/predict?timestamp=1563634800&counterId=151989
