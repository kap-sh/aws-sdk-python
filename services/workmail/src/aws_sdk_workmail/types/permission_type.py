"""Generated from Smithy shape ``com.amazonaws.workmail#PermissionType``."""

from typing import Literal, TypeAlias, cast

PermissionType: TypeAlias = Literal[
    "FULL_ACCESS",
    "SEND_AS",
    "SEND_ON_BEHALF",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PermissionType:
    return cast(PermissionType, data)
