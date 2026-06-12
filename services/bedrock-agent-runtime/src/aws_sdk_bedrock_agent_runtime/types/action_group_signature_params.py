"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupSignatureParams``."""

from typing import TypeAlias

ActionGroupSignatureParams: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionGroupSignatureParams) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ActionGroupSignatureParams:
    out: ActionGroupSignatureParams = {}
    for key, value in data.items():
        out[key] = value
    return out