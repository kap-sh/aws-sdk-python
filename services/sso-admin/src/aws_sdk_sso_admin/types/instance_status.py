"""Generated from Smithy shape ``com.amazonaws.ssoadmin#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

InstanceStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceStatus:
    return cast(InstanceStatus, data)
