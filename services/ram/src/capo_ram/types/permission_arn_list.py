"""Generated from Smithy shape ``com.amazonaws.ram#PermissionArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.string

PermissionArnList: TypeAlias = list["capo_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> PermissionArnList:
    return list(data)
