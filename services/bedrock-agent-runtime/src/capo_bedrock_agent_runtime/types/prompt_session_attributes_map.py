"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PromptSessionAttributesMap``."""

from typing import TypeAlias

PromptSessionAttributesMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PromptSessionAttributesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PromptSessionAttributesMap:
    out: PromptSessionAttributesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
