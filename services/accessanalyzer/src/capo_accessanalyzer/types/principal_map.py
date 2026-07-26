"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PrincipalMap``."""

from typing import TypeAlias

PrincipalMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PrincipalMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PrincipalMap:
    out: PrincipalMap = {}
    for key, value in data.items():
        out[key] = value
    return out
