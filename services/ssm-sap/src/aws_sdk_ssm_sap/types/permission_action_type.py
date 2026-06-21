"""Generated from Smithy shape ``com.amazonaws.ssmsap#PermissionActionType``."""

from typing import Literal, TypeAlias, cast

PermissionActionType: TypeAlias = Literal["RESTORE",]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionActionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionActionType:
    return cast(PermissionActionType, data)
