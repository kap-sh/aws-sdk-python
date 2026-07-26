"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateQueryFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_query_field

MessageTemplateQueryFieldList: TypeAlias = list[
    "capo_qconnect.types.message_template_query_field.MessageTemplateQueryField"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateQueryFieldList) -> list:
    import capo_qconnect.types.message_template_query_field

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.message_template_query_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MessageTemplateQueryFieldList:
    import capo_qconnect.types.message_template_query_field

    out: MessageTemplateQueryFieldList = []
    for item in data:
        out.append(
            capo_qconnect.types.message_template_query_field.deserialize_json(item)
        )
    return out
