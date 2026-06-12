"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaFunctionMemoryMetricName: TypeAlias = Literal["Duration",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Duration",))


def serialize_aws_json_1_0(value: LambdaFunctionMemoryMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMemoryMetricName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaFunctionMemoryMetricName value: {data!r}"
        )
    return cast(LambdaFunctionMemoryMetricName, data)
