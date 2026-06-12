"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryMetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaFunctionMemoryMetricStatistic: TypeAlias = Literal[
    "LowerBound",
    "UpperBound",
    "Expected",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LowerBound",
        "UpperBound",
        "Expected",
    )
)


def serialize_aws_json_1_0(value: LambdaFunctionMemoryMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMemoryMetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaFunctionMemoryMetricStatistic value: {data!r}"
        )
    return cast(LambdaFunctionMemoryMetricStatistic, data)
