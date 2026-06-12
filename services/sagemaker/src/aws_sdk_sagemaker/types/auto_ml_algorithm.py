"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: AutoMLAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLAlgorithm value: {data!r}")
    return cast(AutoMLAlgorithm, data)
