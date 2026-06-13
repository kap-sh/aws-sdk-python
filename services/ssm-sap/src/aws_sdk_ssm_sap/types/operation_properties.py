"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationProperties``."""

from typing import TypeAlias

OperationProperties: TypeAlias = dict["str", "str | None"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: OperationProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> OperationProperties:
    out: OperationProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
