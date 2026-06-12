"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLMetricExtendedEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLMetricExtendedEnum: TypeAlias = Literal[
    "Accuracy",
    "MSE",
    "F1",
    "F1macro",
    "AUC",
    "RMSE",
    "MAE",
    "R2",
    "BalancedAccuracy",
    "Precision",
    "PrecisionMacro",
    "Recall",
    "RecallMacro",
    "LogLoss",
    "InferenceLatency",
    "MAPE",
    "MASE",
    "WAPE",
    "AverageWeightedQuantileLoss",
    "Rouge1",
    "Rouge2",
    "RougeL",
    "RougeLSum",
    "Perplexity",
    "ValidationLoss",
    "TrainingLoss",
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
        "MAE",
        "R2",
        "BalancedAccuracy",
        "Precision",
        "PrecisionMacro",
        "Recall",
        "RecallMacro",
        "LogLoss",
        "InferenceLatency",
        "MAPE",
        "MASE",
        "WAPE",
        "AverageWeightedQuantileLoss",
        "Rouge1",
        "Rouge2",
        "RougeL",
        "RougeLSum",
        "Perplexity",
        "ValidationLoss",
        "TrainingLoss",
    )
)


def serialize_aws_json_1_1(value: AutoMLMetricExtendedEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLMetricExtendedEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLMetricExtendedEnum value: {data!r}")
    return cast(AutoMLMetricExtendedEnum, data)
