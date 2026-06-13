"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_filter_value

MessageTemplateFilterValueList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_filter_value.MessageTemplateFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> MessageTemplateFilterValueList:
    return list(data)
