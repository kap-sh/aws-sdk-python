"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CustomizableMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

CustomizableMetricName: TypeAlias = Literal[
    "CpuUtilization",
    "MemoryUtilization",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CpuUtilization",
        "MemoryUtilization",
    )
)


def serialize_aws_json_1_0(value: CustomizableMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomizableMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomizableMetricName value: {data!r}")
    return cast(CustomizableMetricName, data)
