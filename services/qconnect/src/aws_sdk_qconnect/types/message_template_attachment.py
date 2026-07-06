"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.attachment_file_name
    import aws_sdk_qconnect.types.content_disposition
    import aws_sdk_qconnect.types.url
    import aws_sdk_qconnect.types.uuid


class MessageTemplateAttachment(TypedDict, closed=True):
    content_disposition: "aws_sdk_qconnect.types.content_disposition.ContentDisposition"
    """<p>The presentation information for the attachment file.</p>"""
    name: "aws_sdk_qconnect.types.attachment_file_name.AttachmentFileName"
    """<p>The name of the attachment file being uploaded. The name should include the file extension.</p>"""
    uploaded_time: "datetime.datetime"
    """<p>The timestamp when the attachment file was uploaded.</p>"""
    url: "aws_sdk_qconnect.types.url.Url"
    """<p>A pre-signed Amazon S3 URL that can be used to download the attachment file.</p>"""
    url_expiry: "datetime.datetime"
    """<p>The expiration time of the pre-signed Amazon S3 URL.</p>"""
    attachment_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the attachment file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttachment) -> dict:
    out: dict = {}
    out["contentDisposition"] = value["content_disposition"]
    out["name"] = value["name"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["uploadedTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["uploaded_time"]
    )
    out["url"] = value["url"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["urlExpiry"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["url_expiry"]
    )
    out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_json(data: dict) -> MessageTemplateAttachment:
    out: MessageTemplateAttachment = {}  # type: ignore[typeddict-item]
    if "contentDisposition" in data:
        out["content_disposition"] = data["contentDisposition"]
    else:
        raise DeserializationError(
            "MessageTemplateAttachment.content_disposition required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateAttachment.name required")
    if "uploadedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["uploaded_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["uploadedTime"]
            )
        )
    else:
        raise DeserializationError("MessageTemplateAttachment.uploaded_time required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("MessageTemplateAttachment.url required")
    if "urlExpiry" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["url_expiry"] = aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
            data["urlExpiry"]
        )
    else:
        raise DeserializationError("MessageTemplateAttachment.url_expiry required")
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    else:
        raise DeserializationError("MessageTemplateAttachment.attachment_id required")
    return out
