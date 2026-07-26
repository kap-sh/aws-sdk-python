"""Generated from Smithy shape ``com.amazonaws.qbusiness#FailedAttachmentEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_output
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.message_id


class FailedAttachmentEvent(TypedDict, closed=True):
    conversation_id: NotRequired["capo_qbusiness.types.conversation_id.ConversationId"]
    """<p> The identifier of the conversation associated with the failed file upload.</p>"""
    user_message_id: NotRequired["capo_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of the end user chat message associated with the file upload.</p>"""
    system_message_id: NotRequired["capo_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of the AI-generated message associated with the file upload.</p>"""
    attachment: NotRequired["capo_qbusiness.types.attachment_output.AttachmentOutput"]


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
        import capo_qbusiness.types.attachment_output

        out["attachment"] = capo_qbusiness.types.attachment_output.serialize_json(
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
        import capo_qbusiness.types.attachment_output

        out["attachment"] = capo_qbusiness.types.attachment_output.deserialize_json(
            data["attachment"]
        )
    return out


def serialize_event_json(value: FailedAttachmentEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "failedAttachmentEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> FailedAttachmentEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: FailedAttachmentEvent = {}  # type: ignore[typeddict-item]
    return out
