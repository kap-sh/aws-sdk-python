"""Generated from Smithy shape ``com.amazonaws.pipes#BatchParametersMap``."""

from typing import TypeAlias

BatchParametersMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BatchParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> BatchParametersMap:
    out: BatchParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
