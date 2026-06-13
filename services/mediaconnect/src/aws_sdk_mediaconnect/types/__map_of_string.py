"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__mapOfString``."""

from typing import TypeAlias

__mapOfString: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: __mapOfString) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> __mapOfString:
    out: __mapOfString = {}
    for key, value in data.items():
        out[key] = value
    return out
