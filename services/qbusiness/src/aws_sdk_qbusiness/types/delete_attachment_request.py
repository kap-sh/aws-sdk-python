"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.attachment_id
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.user_id

class DeleteAttachmentRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier for the Amazon Q Business application environment.</p>"""
    conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    """<p>The unique identifier of the conversation.</p>"""
    attachment_id: "aws_sdk_qbusiness.types.attachment_id.AttachmentId"
    """<p>The unique identifier for the attachment.</p>"""
    user_id: NotRequired["aws_sdk_qbusiness.types.user_id.UserId"]
    """<p>The unique identifier of the user involved in the conversation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAttachmentRequest:
    out: DeleteAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out