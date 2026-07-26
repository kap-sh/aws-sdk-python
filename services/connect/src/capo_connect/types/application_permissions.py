"""Generated from Smithy shape ``com.amazonaws.connect#ApplicationPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.permission

ApplicationPermissions: TypeAlias = list["capo_connect.types.permission.Permission"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPermissions) -> list:
    return list(value)


def deserialize_json(data: list) -> ApplicationPermissions:
    return list(data)
