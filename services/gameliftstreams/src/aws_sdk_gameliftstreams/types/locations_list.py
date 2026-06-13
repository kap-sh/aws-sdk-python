"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#LocationsList``."""

from typing import TypeAlias

LocationsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: LocationsList) -> list:
    return list(value)


def deserialize_json(data: list) -> LocationsList:
    return list(data)
