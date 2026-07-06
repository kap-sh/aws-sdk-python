"""Generated from Smithy shape ``com.amazonaws.qbusiness#Attachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_id
    import aws_sdk_qbusiness.types.attachment_name
    import aws_sdk_qbusiness.types.attachment_status
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.copy_from_source
    import aws_sdk_qbusiness.types.error_detail
    import aws_sdk_qbusiness.types.integer
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.timestamp


class Attachment(TypedDict, closed=True):
    attachment_id: NotRequired["aws_sdk_qbusiness.types.attachment_id.AttachmentId"]
    """<p>The identifier of the Amazon Q Business attachment.</p>"""
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p>The identifier of the Amazon Q Business conversation the attachment is associated with.</p>"""
    name: NotRequired["aws_sdk_qbusiness.types.attachment_name.AttachmentName"]
    """<p>Filename of the Amazon Q Business attachment.</p>"""
    copy_from: NotRequired["aws_sdk_qbusiness.types.copy_from_source.CopyFromSource"]
    """<p>A CopyFromSource containing a reference to the original source of the Amazon Q Business attachment.</p>"""
    file_type: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>Filetype of the Amazon Q Business attachment.</p>"""
    file_size: NotRequired["aws_sdk_qbusiness.types.integer.Integer"]
    """<p>Size in bytes of the Amazon Q Business attachment.</p>"""
    md5chksum: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>MD5 checksum of the Amazon Q Business attachment contents.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business attachment was created.</p>"""
    status: NotRequired["aws_sdk_qbusiness.types.attachment_status.AttachmentStatus"]
    """<p>AttachmentStatus of the Amazon Q Business attachment.</p>"""
    error: NotRequired["aws_sdk_qbusiness.types.error_detail.ErrorDetail"]
    """<p>ErrorDetail providing information about a Amazon Q Business attachment error. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attachment) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "copy_from" in value:
        import aws_sdk_qbusiness.types.copy_from_source

        out["copyFrom"] = aws_sdk_qbusiness.types.copy_from_source.serialize_json(
            value["copy_from"]
        )
    if "file_type" in value:
        out["fileType"] = value["file_type"]
    if "file_size" in value:
        out["fileSize"] = value["file_size"]
    if "md5chksum" in value:
        out["md5chksum"] = value["md5chksum"]
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
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
    return out


def deserialize_json(data: dict) -> Attachment:
    out: Attachment = {}  # type: ignore[typeddict-item]
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    if "name" in data:
        out["name"] = data["name"]
    if "copyFrom" in data:
        import aws_sdk_qbusiness.types.copy_from_source

        out["copy_from"] = aws_sdk_qbusiness.types.copy_from_source.deserialize_json(
            data["copyFrom"]
        )
    if "fileType" in data:
        out["file_type"] = data["fileType"]
    if "fileSize" in data:
        out["file_size"] = data["fileSize"]
    if "md5chksum" in data:
        out["md5chksum"] = data["md5chksum"]
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
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
    return out
