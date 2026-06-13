"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_version_summary

MessageTemplateVersionSummaryList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_version_summary.MessageTemplateVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateVersionSummaryList) -> list:
    import aws_sdk_qconnect.types.message_template_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.message_template_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MessageTemplateVersionSummaryList:
    import aws_sdk_qconnect.types.message_template_version_summary

    out: MessageTemplateVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.message_template_version_summary.deserialize_json(
                item
            )
        )
    return out
