"""Generated from Smithy shape ``com.amazonaws.signin#Principal``."""

from typing import TypeAlias

Principal: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Principal) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Principal:
    out: Principal = {}
    for key, value in data.items():
        out[key] = value
    return out
