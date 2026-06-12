"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AttributeMap``."""

from typing import TypeAlias

AttributeMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AttributeMap:
    out: AttributeMap = {}
    for key, value in data.items():
        out[key] = value
    return out