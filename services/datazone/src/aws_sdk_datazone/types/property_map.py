"""Generated from Smithy shape ``com.amazonaws.datazone#PropertyMap``."""

from typing import TypeAlias

PropertyMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PropertyMap:
    out: PropertyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
