"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetDocumentContentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.string


class GetDocumentContentResponse(TypedDict):
    presigned_url: "aws_sdk_qbusiness.types.string.String"
    """<p>A pre-signed URL that provides temporary access to download the document content directly from Amazon Q Business. The URL expires after 5 minutes for security purposes. This URL is generated only after successful ACL validation.</p>"""
    mime_type: "aws_sdk_qbusiness.types.string.String"
    """<p>The MIME type of the document content. When outputFormat is RAW, this corresponds to the original document's MIME type (e.g., application/pdf, text/plain, application/vnd.openxmlformats-officedocument.wordprocessingml.document). When outputFormat is EXTRACTED, the MIME type is always application/json.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentContentResponse) -> dict:
    out: dict = {}
    out["presignedUrl"] = value["presigned_url"]
    out["mimeType"] = value["mime_type"]
    return out


def deserialize_json(data: dict) -> GetDocumentContentResponse:
    out: GetDocumentContentResponse = {}  # type: ignore[typeddict-item]
    if "presignedUrl" in data:
        out["presigned_url"] = data["presignedUrl"]
    else:
        raise DeserializationError("GetDocumentContentResponse.presigned_url required")
    if "mimeType" in data:
        out["mime_type"] = data["mimeType"]
    else:
        raise DeserializationError("GetDocumentContentResponse.mime_type required")
    return out
