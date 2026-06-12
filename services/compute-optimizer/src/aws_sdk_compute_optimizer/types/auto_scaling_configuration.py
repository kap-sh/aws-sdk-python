"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingConfiguration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

AutoScalingConfiguration: TypeAlias = Literal[
    "TargetTrackingScalingCpu",
    "TargetTrackingScalingMemory",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TargetTrackingScalingCpu",
        "TargetTrackingScalingMemory",
    )
)


def serialize_aws_json_1_0(value: AutoScalingConfiguration) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoScalingConfiguration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoScalingConfiguration value: {data!r}")
    return cast(AutoScalingConfiguration, data)
