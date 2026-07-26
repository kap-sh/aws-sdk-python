"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDeleteDelegationByAssessmentError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.error_code
    import capo_auditmanager.types.error_message
    import capo_auditmanager.types.uuid


class BatchDeleteDelegationByAssessmentError(TypedDict, closed=True):
    delegation_id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the delegation. </p>"""
    error_code: NotRequired["capo_auditmanager.types.error_code.ErrorCode"]
    """<p> The error code that the <code>BatchDeleteDelegationByAssessment</code> API returned. </p>"""
    error_message: NotRequired["capo_auditmanager.types.error_message.ErrorMessage"]
    """<p> The error message that the <code>BatchDeleteDelegationByAssessment</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDelegationByAssessmentError) -> dict:
    out: dict = {}
    if "delegation_id" in value:
        out["delegationId"] = value["delegation_id"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteDelegationByAssessmentError:
    out: BatchDeleteDelegationByAssessmentError = {}  # type: ignore[typeddict-item]
    if "delegationId" in data:
        out["delegation_id"] = data["delegationId"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
