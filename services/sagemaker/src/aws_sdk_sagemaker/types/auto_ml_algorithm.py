"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLAlgorithm``."""

from typing import Literal, TypeAlias, cast

AutoMLAlgorithm: TypeAlias = Literal[
    "xgboost",
    "linear-learner",
    "mlp",
    "lightgbm",
    "catboost",
    "randomforest",
    "extra-trees",
    "nn-torch",
    "fastai",
    "cnn-qr",
    "deepar",
    "prophet",
    "npts",
    "arima",
    "ets",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLAlgorithm:
    return cast(AutoMLAlgorithm, data)
