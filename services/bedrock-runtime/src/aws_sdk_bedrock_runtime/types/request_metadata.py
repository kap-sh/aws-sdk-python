"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#RequestMetadata``."""

from typing import TypeAlias

RequestMetadata: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RequestMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RequestMetadata:
    out: RequestMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
