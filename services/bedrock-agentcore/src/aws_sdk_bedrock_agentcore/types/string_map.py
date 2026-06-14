"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StringMap``."""

from typing import TypeAlias

StringMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StringMap:
    out: StringMap = {}
    for key, value in data.items():
        out[key] = value
    return out
