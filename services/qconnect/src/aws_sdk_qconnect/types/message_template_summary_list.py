"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_summary

MessageTemplateSummaryList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_summary.MessageTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSummaryList) -> list:
    import aws_sdk_qconnect.types.message_template_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.message_template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageTemplateSummaryList:
    import aws_sdk_qconnect.types.message_template_summary

    out: MessageTemplateSummaryList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.message_template_summary.deserialize_json(item)
        )
    return out
