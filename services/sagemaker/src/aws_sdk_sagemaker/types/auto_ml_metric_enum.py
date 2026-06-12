"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLMetricEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLMetricEnum: TypeAlias = Literal[
    "Accuracy",
    "MSE",
    "F1",
    "F1macro",
    "AUC",
    "RMSE",
    "BalancedAccuracy",
    "R2",
    "Recall",
    "RecallMacro",
    "Precision",
    "PrecisionMacro",
    "MAE",
    "MAPE",
    "MASE",
    "WAPE",
    "AverageWeightedQuantileLoss",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Accuracy",
        "MSE",
        "F1",
        "F1macro",
        "AUC",
        "RMSE",
        "BalancedAccuracy",
        "R2",
        "Recall",
        "RecallMacro",
        "Precision",
        "PrecisionMacro",
        "MAE",
        "MAPE",
        "MASE",
        "WAPE",
        "AverageWeightedQuantileLoss",
    )
)


def serialize_aws_json_1_1(value: AutoMLMetricEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLMetricEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLMetricEnum value: {data!r}")
    return cast(AutoMLMetricEnum, data)
