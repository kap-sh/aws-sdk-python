"""Generated from Smithy shape ``com.amazonaws.connect#PermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.security_profile_permission

PermissionsList: TypeAlias = list[
    "aws_sdk_connect.types.security_profile_permission.SecurityProfilePermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> PermissionsList:
    return list(data)
