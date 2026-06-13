"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attachment

MessageTemplateAttachmentList: TypeAlias = list[
    "aws_sdk_qconnect.types.message_template_attachment.MessageTemplateAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttachmentList) -> list:
    import aws_sdk_qconnect.types.message_template_attachment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.message_template_attachment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MessageTemplateAttachmentList:
    import aws_sdk_qconnect.types.message_template_attachment

    out: MessageTemplateAttachmentList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.message_template_attachment.deserialize_json(item)
        )
    return out
