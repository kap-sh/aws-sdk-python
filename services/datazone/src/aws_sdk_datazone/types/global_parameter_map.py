"""Generated from Smithy shape ``com.amazonaws.datazone#GlobalParameterMap``."""

from typing import TypeAlias

GlobalParameterMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: GlobalParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> GlobalParameterMap:
    out: GlobalParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
