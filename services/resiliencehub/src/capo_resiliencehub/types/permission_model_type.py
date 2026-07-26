"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PermissionModelType``."""

from typing import Literal, TypeAlias, cast

PermissionModelType: TypeAlias = Literal[
    "LegacyIAMUser",
    "RoleBased",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionModelType) -> str:
    return value


def deserialize_json(data: str) -> PermissionModelType:
    return cast(PermissionModelType, data)
