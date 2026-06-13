"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DataMap``."""

from typing import TypeAlias

DataMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DataMap:
    out: DataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
