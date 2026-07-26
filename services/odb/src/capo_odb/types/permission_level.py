"""Generated from Smithy shape ``com.amazonaws.odb#PermissionLevel``."""

from typing import Literal, TypeAlias, cast

PermissionLevel: TypeAlias = Literal[
    "RESTRICTED",
    "UNRESTRICTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PermissionLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PermissionLevel:
    return cast(PermissionLevel, data)
