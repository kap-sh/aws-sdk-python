"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#InstancePropertyMap``."""

from typing import TypeAlias

InstancePropertyMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InstancePropertyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> InstancePropertyMap:
    out: InstancePropertyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
