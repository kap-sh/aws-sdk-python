"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FeaturesMap``."""

from typing import TypeAlias

FeaturesMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FeaturesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FeaturesMap:
    out: FeaturesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
