"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportEvidenceError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.error_code
    import capo_auditmanager.types.error_message
    import capo_auditmanager.types.uuid


class AssessmentReportEvidenceError(TypedDict, closed=True):
    evidence_id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the evidence. </p>"""
    error_code: NotRequired["capo_auditmanager.types.error_code.ErrorCode"]
    """<p> The error code that was returned. </p>"""
    error_message: NotRequired["capo_auditmanager.types.error_message.ErrorMessage"]
    """<p> The error message that was returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportEvidenceError) -> dict:
    out: dict = {}
    if "evidence_id" in value:
        out["evidenceId"] = value["evidence_id"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> AssessmentReportEvidenceError:
    out: AssessmentReportEvidenceError = {}  # type: ignore[typeddict-item]
    if "evidenceId" in data:
        out["evidence_id"] = data["evidenceId"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
