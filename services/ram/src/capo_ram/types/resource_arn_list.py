"""Generated from Smithy shape ``com.amazonaws.ram#ResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.string

ResourceArnList: TypeAlias = list["capo_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArnList:
    return list(data)
