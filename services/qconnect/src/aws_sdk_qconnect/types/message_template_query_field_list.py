"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateQueryFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_query_field

MessageTemplateQueryFieldList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_query_field.MessageTemplateQueryField"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateQueryFieldList) -> list:
    import aws_sdk_qconnect.types.message_template_query_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.message_template_query_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MessageTemplateQueryFieldList:
    import aws_sdk_qconnect.types.message_template_query_field

    out: MessageTemplateQueryFieldList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.message_template_query_field.deserialize_json(item)
        )
    return out
