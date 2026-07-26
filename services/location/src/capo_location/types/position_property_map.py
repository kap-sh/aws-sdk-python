"""Generated from Smithy shape ``com.amazonaws.location#PositionPropertyMap``."""

from typing import TypeAlias

PositionPropertyMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PositionPropertyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PositionPropertyMap:
    out: PositionPropertyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
