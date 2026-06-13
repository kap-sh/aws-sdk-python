"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSearchResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_search_result_data

MessageTemplateSearchResultsList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_search_result_data.MessageTemplateSearchResultData"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSearchResultsList) -> list:
    import aws_sdk_qconnect.types.message_template_search_result_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.message_template_search_result_data.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MessageTemplateSearchResultsList:
    import aws_sdk_qconnect.types.message_template_search_result_data

    out: MessageTemplateSearchResultsList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.message_template_search_result_data.deserialize_json(
                item
            )
        )
    return out
