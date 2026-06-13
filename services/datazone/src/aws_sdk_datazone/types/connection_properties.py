"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionProperties``."""

from typing import TypeAlias

ConnectionProperties: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConnectionProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConnectionProperties:
    out: ConnectionProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
