"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceConfigurationParameterMap``."""

from typing import TypeAlias

ResourceConfigurationParameterMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceConfigurationParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResourceConfigurationParameterMap:
    out: ResourceConfigurationParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
