"""Generated from Smithy shape ``com.amazonaws.workdocs#RolePermissionType``."""

from typing import Literal, TypeAlias, cast

RolePermissionType: TypeAlias = Literal[
    "DIRECT",
    "INHERITED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RolePermissionType) -> str:
    return value


def deserialize_json(data: str) -> RolePermissionType:
    return cast(RolePermissionType, data)
