"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentOverridesValue``."""

from typing import TypeAlias

ComponentOverridesValue: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentOverridesValue) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ComponentOverridesValue:
    out: ComponentOverridesValue = {}
    for key, value in data.items():
        out[key] = value
    return out
