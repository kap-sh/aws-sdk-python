"""Generated from Smithy shape ``com.amazonaws.connectcases#Tags``."""

from typing import TypeAlias

Tags: TypeAlias = dict["str", "str | None"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
