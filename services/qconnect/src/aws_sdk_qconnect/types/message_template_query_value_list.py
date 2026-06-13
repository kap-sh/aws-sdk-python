"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateQueryValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_query_value

MessageTemplateQueryValueList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_query_value.MessageTemplateQueryValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateQueryValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> MessageTemplateQueryValueList:
    return list(data)
