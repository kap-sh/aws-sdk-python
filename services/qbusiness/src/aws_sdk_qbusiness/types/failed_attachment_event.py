"""Generated from Smithy shape ``com.amazonaws.qbusiness#FailedAttachmentEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_output
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.message_id


class FailedAttachmentEvent(TypedDict):
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p> The identifier of the conversation associated with the failed file upload.</p>"""
    user_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of the end user chat message associated with the file upload.</p>"""
    system_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of the AI-generated message associated with the file upload.</p>"""
    attachment: NotRequired[
        "aws_sdk_qbusiness.types.attachment_output.AttachmentOutput"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FailedAttachmentEvent) -> dict:
    out: dict = {}
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "user_message_id" in value:
        out["userMessageId"] = value["user_message_id"]
    if "system_message_id" in value:
        out["systemMessageId"] = value["system_message_id"]
    if "attachment" in value:
        import aws_sdk_qbusiness.types.attachment_output

        out["attachment"] = aws_sdk_qbusiness.types.attachment_output.serialize_json(
            value["attachment"]
        )
    return out


def deserialize_json(data: dict) -> FailedAttachmentEvent:
    out: FailedAttachmentEvent = {}  # type: ignore[typeddict-item]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    if "userMessageId" in data:
        out["user_message_id"] = data["userMessageId"]
    if "systemMessageId" in data:
        out["system_message_id"] = data["systemMessageId"]
    if "attachment" in data:
        import aws_sdk_qbusiness.types.attachment_output

        out["attachment"] = aws_sdk_qbusiness.types.attachment_output.deserialize_json(
            data["attachment"]
        )
    return out
