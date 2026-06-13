"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttributeKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attribute_key

MessageTemplateAttributeKeyList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_attribute_key.MessageTemplateAttributeKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttributeKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> MessageTemplateAttributeKeyList:
    return list(data)
