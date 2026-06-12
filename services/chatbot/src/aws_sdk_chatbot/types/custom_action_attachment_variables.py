"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachmentVariables``."""

from typing import TypeAlias

CustomActionAttachmentVariables: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomActionAttachmentVariables) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomActionAttachmentVariables:
    out: CustomActionAttachmentVariables = {}
    for key, value in data.items():
        out[key] = value
    return out
