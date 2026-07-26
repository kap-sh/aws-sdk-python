"""Generated from Smithy shape ``com.amazonaws.forecast#OptimizationMetric``."""

from typing import Literal, TypeAlias, cast

OptimizationMetric: TypeAlias = Literal[
    "WAPE",
    "RMSE",
    "AverageWeightedQuantileLoss",
    "MASE",
    "MAPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationMetric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptimizationMetric:
    return cast(OptimizationMetric, data)
