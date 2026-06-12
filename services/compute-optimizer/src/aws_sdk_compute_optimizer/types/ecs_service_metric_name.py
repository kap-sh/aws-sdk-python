"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ECSServiceMetricName: TypeAlias = Literal[
    "Cpu",
    "Memory",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cpu",
        "Memory",
    )
)


def serialize_aws_json_1_0(value: ECSServiceMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ECSServiceMetricName value: {data!r}")
    return cast(ECSServiceMetricName, data)
