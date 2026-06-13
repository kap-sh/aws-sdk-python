"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttributeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attribute_type

MessageTemplateAttributeTypeList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_attribute_type.MessageTemplateAttributeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttributeTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> MessageTemplateAttributeTypeList:
    return list(data)
