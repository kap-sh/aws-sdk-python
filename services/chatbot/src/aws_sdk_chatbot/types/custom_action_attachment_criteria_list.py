"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachmentCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_attachment_criteria

CustomActionAttachmentCriteriaList: TypeAlias = list[
    "aws_sdk_chatbot.types.custom_action_attachment_criteria.CustomActionAttachmentCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionAttachmentCriteriaList) -> list:
    import aws_sdk_chatbot.types.custom_action_attachment_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chatbot.types.custom_action_attachment_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CustomActionAttachmentCriteriaList:
    import aws_sdk_chatbot.types.custom_action_attachment_criteria

    out: CustomActionAttachmentCriteriaList = []
    for item in data:
        out.append(
            aws_sdk_chatbot.types.custom_action_attachment_criteria.deserialize_json(
                item
            )
        )
    return out
