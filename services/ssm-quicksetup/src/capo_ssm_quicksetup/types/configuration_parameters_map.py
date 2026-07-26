"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationParametersMap``."""

from typing import TypeAlias

ConfigurationParametersMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConfigurationParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConfigurationParametersMap:
    out: ConfigurationParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
