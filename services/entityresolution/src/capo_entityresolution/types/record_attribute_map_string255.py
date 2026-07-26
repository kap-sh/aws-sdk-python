"""Generated from Smithy shape ``com.amazonaws.entityresolution#RecordAttributeMapString255``."""

from typing import TypeAlias

RecordAttributeMapString255: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RecordAttributeMapString255) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RecordAttributeMapString255:
    out: RecordAttributeMapString255 = {}
    for key, value in data.items():
        out[key] = value
    return out
