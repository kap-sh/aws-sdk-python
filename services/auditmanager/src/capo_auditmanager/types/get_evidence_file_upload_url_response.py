"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFileUploadUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.non_empty_string


class GetEvidenceFileUploadUrlResponse(TypedDict, closed=True):
    evidence_file_name: NotRequired[
        "capo_auditmanager.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the uploaded manual evidence file that the presigned URL was generated for.</p>"""
    upload_url: NotRequired["capo_auditmanager.types.non_empty_string.NonEmptyString"]
    """<p>The presigned URL that was generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFileUploadUrlResponse) -> dict:
    out: dict = {}
    if "evidence_file_name" in value:
        out["evidenceFileName"] = value["evidence_file_name"]
    if "upload_url" in value:
        out["uploadUrl"] = value["upload_url"]
    return out


def deserialize_json(data: dict) -> GetEvidenceFileUploadUrlResponse:
    out: GetEvidenceFileUploadUrlResponse = {}  # type: ignore[typeddict-item]
    if "evidenceFileName" in data:
        out["evidence_file_name"] = data["evidenceFileName"]
    if "uploadUrl" in data:
        out["upload_url"] = data["uploadUrl"]
    return out
