"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseAttachmentDownloadUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.attachment_id
    import capo_security_ir.types.case_id


class GetCaseAttachmentDownloadUrlRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element for GetCaseAttachmentDownloadUrl to identify the case ID for downloading an attachment from. </p>"""
    attachment_id: "capo_security_ir.types.attachment_id.AttachmentId"
    """<p>Required element for GetCaseAttachmentDownloadUrl to identify the attachment ID for downloading an attachment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAttachmentDownloadUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCaseAttachmentDownloadUrlRequest:
    out: GetCaseAttachmentDownloadUrlRequest = {}  # type: ignore[typeddict-item]
    return out
