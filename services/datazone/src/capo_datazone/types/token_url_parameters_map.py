"""Generated from Smithy shape ``com.amazonaws.datazone#TokenUrlParametersMap``."""

from typing import TypeAlias

TokenUrlParametersMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TokenUrlParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TokenUrlParametersMap:
    out: TokenUrlParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
