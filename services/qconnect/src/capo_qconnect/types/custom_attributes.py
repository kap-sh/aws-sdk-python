"""Generated from Smithy shape ``com.amazonaws.qconnect#CustomAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_key
    import capo_qconnect.types.message_template_attribute_value

CustomAttributes: TypeAlias = dict[
    "capo_qconnect.types.message_template_attribute_key.MessageTemplateAttributeKey",
    "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomAttributes:
    out: CustomAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
