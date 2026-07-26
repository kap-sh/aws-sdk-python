"""Generated from Smithy shape ``com.amazonaws.location#DeviceIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.id

DeviceIdsList: TypeAlias = list["capo_location.types.id.Id"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeviceIdsList:
    return list(data)
