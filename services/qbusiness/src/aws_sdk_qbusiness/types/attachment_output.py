"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_id
    import aws_sdk_qbusiness.types.attachment_name
    import aws_sdk_qbusiness.types.attachment_status
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.error_detail


class AttachmentOutput(TypedDict, closed=True):
    name: NotRequired["aws_sdk_qbusiness.types.attachment_name.AttachmentName"]
    """<p>The name of a file uploaded during chat.</p>"""
    status: NotRequired["aws_sdk_qbusiness.types.attachment_status.AttachmentStatus"]
    """<p>The status of a file uploaded during chat.</p>"""
    error: NotRequired["aws_sdk_qbusiness.types.error_detail.ErrorDetail"]
    """<p>An error associated with a file uploaded during chat.</p>"""
    attachment_id: NotRequired["aws_sdk_qbusiness.types.attachment_id.AttachmentId"]
    """<p>The unique identifier of the Amazon Q Business attachment.</p>"""
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p>The unique identifier of the Amazon Q Business conversation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import aws_sdk_qbusiness.types.attachment_status

        out["status"] = aws_sdk_qbusiness.types.attachment_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.serialize_json(
            value["error"]
        )
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    return out


def deserialize_json(data: dict) -> AttachmentOutput:
    out: AttachmentOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_qbusiness.types.attachment_status

        out["status"] = aws_sdk_qbusiness.types.attachment_status.deserialize_json(
            data["status"]
        )
    if "error" in data:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.deserialize_json(
            data["error"]
        )
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    return out
