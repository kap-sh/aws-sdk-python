"""Generated from Smithy shape ``com.amazonaws.backupsearch#TagMap``."""

from typing import TypeAlias

TagMap: TypeAlias = dict["str", "str | None"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
