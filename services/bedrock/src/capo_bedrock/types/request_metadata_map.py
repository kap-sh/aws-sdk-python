"""Generated from Smithy shape ``com.amazonaws.bedrock#RequestMetadataMap``."""

from typing import TypeAlias

RequestMetadataMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RequestMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RequestMetadataMap:
    out: RequestMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
