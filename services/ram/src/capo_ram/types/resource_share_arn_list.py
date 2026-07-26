"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.string

ResourceShareArnList: TypeAlias = list["capo_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceShareArnList:
    return list(data)
