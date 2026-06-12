"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaFunctionMetricStatistic: TypeAlias = Literal[
    "Maximum",
    "Average",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Maximum",
        "Average",
    )
)


def serialize_aws_json_1_0(value: LambdaFunctionMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaFunctionMetricStatistic value: {data!r}"
        )
    return cast(LambdaFunctionMetricStatistic, data)
