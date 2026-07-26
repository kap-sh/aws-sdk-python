"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataMap``."""

from typing import TypeAlias

MetadataMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MetadataMap:
    out: MetadataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
