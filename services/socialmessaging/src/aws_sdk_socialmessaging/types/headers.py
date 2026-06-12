"""Generated from Smithy shape ``com.amazonaws.socialmessaging#Headers``."""

from typing import TypeAlias

Headers: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Headers) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Headers:
    out: Headers = {}
    for key, value in data.items():
        out[key] = value
    return out
