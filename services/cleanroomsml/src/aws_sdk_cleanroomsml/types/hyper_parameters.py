"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#HyperParameters``."""

from typing import TypeAlias

HyperParameters: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HyperParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> HyperParameters:
    out: HyperParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
