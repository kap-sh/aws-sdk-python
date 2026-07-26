"""Generated from Smithy shape ``com.amazonaws.neptunedata#StringValuedMap``."""

from typing import TypeAlias

StringValuedMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StringValuedMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StringValuedMap:
    out: StringValuedMap = {}
    for key, value in data.items():
        out[key] = value
    return out
