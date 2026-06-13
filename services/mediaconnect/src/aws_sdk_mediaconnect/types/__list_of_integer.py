"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfInteger``."""

from typing import TypeAlias

__listOfInteger: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInteger) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOfInteger:
    return list(data)
