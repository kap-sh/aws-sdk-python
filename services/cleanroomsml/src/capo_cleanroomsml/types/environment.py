"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#Environment``."""

from typing import TypeAlias

Environment: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Environment) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Environment:
    out: Environment = {}
    for key, value in data.items():
        out[key] = value
    return out
