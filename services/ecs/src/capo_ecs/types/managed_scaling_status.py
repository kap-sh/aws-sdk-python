"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedScalingStatus``."""

from typing import Literal, TypeAlias, cast

ManagedScalingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedScalingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedScalingStatus:
    return cast(ManagedScalingStatus, data)
