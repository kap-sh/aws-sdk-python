"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_attachment

CustomActionAttachmentList: TypeAlias = list[
    "aws_sdk_chatbot.types.custom_action_attachment.CustomActionAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionAttachmentList) -> list:
    import aws_sdk_chatbot.types.custom_action_attachment

    out: list = []
    for item in value:
        out.append(aws_sdk_chatbot.types.custom_action_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomActionAttachmentList:
    import aws_sdk_chatbot.types.custom_action_attachment

    out: CustomActionAttachmentList = []
    for item in data:
        out.append(
            aws_sdk_chatbot.types.custom_action_attachment.deserialize_json(item)
        )
    return out
