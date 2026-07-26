"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InferenceEnvironmentMap``."""

from typing import TypeAlias

InferenceEnvironmentMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InferenceEnvironmentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> InferenceEnvironmentMap:
    out: InferenceEnvironmentMap = {}
    for key, value in data.items():
        out[key] = value
    return out
