"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthState``."""

from typing import Literal, TypeAlias, cast

InstanceHealthState: TypeAlias = Literal[
    "initial",
    "healthy",
    "unhealthy",
    "unused",
    "draining",
    "unavailable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthState:
    return cast(InstanceHealthState, data)
