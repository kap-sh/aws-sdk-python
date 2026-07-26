"""Generated from Smithy shape ``com.amazonaws.neptunegraph#LongValuedMap``."""

from typing import TypeAlias

LongValuedMap: TypeAlias = dict["str", "int"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LongValuedMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> LongValuedMap:
    out: LongValuedMap = {}
    for key, value in data.items():
        out[key] = value
    return out
