"""Generated from Smithy shape ``com.amazonaws.oam#TagMapOutput``."""

from typing import TypeAlias

TagMapOutput: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMapOutput) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMapOutput:
    out: TagMapOutput = {}
    for key, value in data.items():
        out[key] = value
    return out
