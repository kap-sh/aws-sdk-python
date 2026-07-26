"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

InstanceStatus: TypeAlias = Literal[
    "IN_USE",
    "PREPARING",
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceStatus:
    return cast(InstanceStatus, data)
