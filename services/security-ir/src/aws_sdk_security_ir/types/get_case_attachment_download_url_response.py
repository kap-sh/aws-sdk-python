"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseAttachmentDownloadUrlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.url


class GetCaseAttachmentDownloadUrlResponse(TypedDict):
    attachment_presigned_url: "aws_sdk_security_ir.types.url.Url"
    """<p>Response element providing the Amazon S3 presigned URL to download an attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAttachmentDownloadUrlResponse) -> dict:
    out: dict = {}
    out["attachmentPresignedUrl"] = value["attachment_presigned_url"]
    return out


def deserialize_json(data: dict) -> GetCaseAttachmentDownloadUrlResponse:
    out: GetCaseAttachmentDownloadUrlResponse = {}  # type: ignore[typeddict-item]
    if "attachmentPresignedUrl" in data:
        out["attachment_presigned_url"] = data["attachmentPresignedUrl"]
    else:
        raise DeserializationError(
            "GetCaseAttachmentDownloadUrlResponse.attachment_presigned_url required"
        )
    return out
