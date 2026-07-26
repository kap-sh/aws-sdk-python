"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.error_code
    import capo_auditmanager.types.error_message
    import capo_auditmanager.types.manual_evidence


class BatchImportEvidenceToAssessmentControlError(TypedDict, closed=True):
    manual_evidence: NotRequired[
        "capo_auditmanager.types.manual_evidence.ManualEvidence"
    ]
    """<p> Manual evidence that can't be collected automatically by Audit Manager. </p>"""
    error_code: NotRequired["capo_auditmanager.types.error_code.ErrorCode"]
    """<p> The error code that the <code>BatchImportEvidenceToAssessmentControl</code> API returned. </p>"""
    error_message: NotRequired["capo_auditmanager.types.error_message.ErrorMessage"]
    """<p> The error message that the <code>BatchImportEvidenceToAssessmentControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlError) -> dict:
    out: dict = {}
    if "manual_evidence" in value:
        import capo_auditmanager.types.manual_evidence

        out["manualEvidence"] = capo_auditmanager.types.manual_evidence.serialize_json(
            value["manual_evidence"]
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchImportEvidenceToAssessmentControlError:
    out: BatchImportEvidenceToAssessmentControlError = {}  # type: ignore[typeddict-item]
    if "manualEvidence" in data:
        import capo_auditmanager.types.manual_evidence

        out["manual_evidence"] = (
            capo_auditmanager.types.manual_evidence.deserialize_json(
                data["manualEvidence"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
