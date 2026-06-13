"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfString``."""

from typing import TypeAlias

__listOfString: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfString) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOfString:
    return list(data)
