"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionAttributesMap``."""

from typing import TypeAlias

SessionAttributesMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SessionAttributesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SessionAttributesMap:
    out: SessionAttributesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
