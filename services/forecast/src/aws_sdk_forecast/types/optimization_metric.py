"""Generated from Smithy shape ``com.amazonaws.forecast#OptimizationMetric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

OptimizationMetric: TypeAlias = Literal[
    "WAPE",
    "RMSE",
    "AverageWeightedQuantileLoss",
    "MASE",
    "MAPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WAPE",
        "RMSE",
        "AverageWeightedQuantileLoss",
        "MASE",
        "MAPE",
    )
)


def serialize_aws_json_1_1(value: OptimizationMetric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptimizationMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptimizationMetric value: {data!r}")
    return cast(OptimizationMetric, data)
