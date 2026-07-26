"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateFilterFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_filter_field

MessageTemplateFilterFieldList: TypeAlias = list[
    "capo_qconnect.types.message_template_filter_field.MessageTemplateFilterField"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateFilterFieldList) -> list:
    import capo_qconnect.types.message_template_filter_field

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.message_template_filter_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MessageTemplateFilterFieldList:
    import capo_qconnect.types.message_template_filter_field

    out: MessageTemplateFilterFieldList = []
    for item in data:
        out.append(
            capo_qconnect.types.message_template_filter_field.deserialize_json(item)
        )
    return out
