"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.custom_action_attachment

CustomActionAttachmentList: TypeAlias = list[
    "capo_chatbot.types.custom_action_attachment.CustomActionAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionAttachmentList) -> list:
    import capo_chatbot.types.custom_action_attachment

    out: list = []
    for item in value:
        out.append(capo_chatbot.types.custom_action_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomActionAttachmentList:
    import capo_chatbot.types.custom_action_attachment

    out: CustomActionAttachmentList = []
    for item in data:
        out.append(capo_chatbot.types.custom_action_attachment.deserialize_json(item))
    return out
