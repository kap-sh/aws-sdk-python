"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseAttachmentUploadUrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id
    import aws_sdk_security_ir.types.content_length
    import aws_sdk_security_ir.types.file_name


class GetCaseAttachmentUploadUrlRequest(TypedDict):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Required element for GetCaseAttachmentUploadUrl to identify the case ID for uploading an attachment. </p>"""
    file_name: "aws_sdk_security_ir.types.file_name.FileName"
    """<p>Required element for GetCaseAttachmentUploadUrl to identify the file name of the attachment to upload. </p>"""
    content_length: "aws_sdk_security_ir.types.content_length.ContentLength"
    """<p>Required element for GetCaseAttachmentUploadUrl to identify the size of the file attachment.</p>"""
    client_token: NotRequired["str"]
    """<note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAttachmentUploadUrlRequest) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    out["contentLength"] = value["content_length"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> GetCaseAttachmentUploadUrlRequest:
    out: GetCaseAttachmentUploadUrlRequest = {}  # type: ignore[typeddict-item]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError(
            "GetCaseAttachmentUploadUrlRequest.file_name required"
        )
    if "contentLength" in data:
        out["content_length"] = data["contentLength"]
    else:
        raise DeserializationError(
            "GetCaseAttachmentUploadUrlRequest.content_length required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
