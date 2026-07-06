"""Generated from Smithy shape ``com.amazonaws.qbusiness#ConversationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_id
    import aws_sdk_qbusiness.types.conversation_id


class ConversationSource(TypedDict, closed=True):
    conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    """<p>The unique identifier of the Amazon Q Business conversation.</p>"""
    attachment_id: "aws_sdk_qbusiness.types.attachment_id.AttachmentId"
    """<p>The unique identifier of the Amazon Q Business attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationSource) -> dict:
    out: dict = {}
    out["conversationId"] = value["conversation_id"]
    out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_json(data: dict) -> ConversationSource:
    out: ConversationSource = {}  # type: ignore[typeddict-item]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    else:
        raise DeserializationError("ConversationSource.conversation_id required")
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    else:
        raise DeserializationError("ConversationSource.attachment_id required")
    return out
