"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLMetricExtendedEnum``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: AutoMLMetricExtendedEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLMetricExtendedEnum:
    return cast(AutoMLMetricExtendedEnum, data)
