"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaFunctionMetricName: TypeAlias = Literal[
    "Duration",
    "Memory",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Duration",
        "Memory",
    )
)


def serialize_aws_json_1_0(value: LambdaFunctionMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LambdaFunctionMetricName value: {data!r}")
    return cast(LambdaFunctionMetricName, data)
