"""Generated from Smithy shape ``com.amazonaws.datazone#RegionalParameter``."""

from typing import TypeAlias

RegionalParameter: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RegionalParameter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RegionalParameter:
    out: RegionalParameter = {}
    for key, value in data.items():
        out[key] = value
    return out
