"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FieldMap``."""

from typing import TypeAlias

FieldMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FieldMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FieldMap:
    out: FieldMap = {}
    for key, value in data.items():
        out[key] = value
    return out
