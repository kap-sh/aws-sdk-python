"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchAssociateAssessmentReportEvidenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_report_evidence_errors
    import capo_auditmanager.types.evidence_ids


class BatchAssociateAssessmentReportEvidenceResponse(TypedDict, closed=True):
    evidence_ids: NotRequired["capo_auditmanager.types.evidence_ids.EvidenceIds"]
    """<p> The list of evidence identifiers. </p>"""
    errors: NotRequired[
        "capo_auditmanager.types.assessment_report_evidence_errors.AssessmentReportEvidenceErrors"
    ]
    """<p> A list of errors that the <code>BatchAssociateAssessmentReportEvidence</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateAssessmentReportEvidenceResponse) -> dict:
    out: dict = {}
    if "evidence_ids" in value:
        import capo_auditmanager.types.evidence_ids

        out["evidenceIds"] = capo_auditmanager.types.evidence_ids.serialize_json(
            value["evidence_ids"]
        )
    if "errors" in value:
        import capo_auditmanager.types.assessment_report_evidence_errors

        out["errors"] = (
            capo_auditmanager.types.assessment_report_evidence_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateAssessmentReportEvidenceResponse:
    out: BatchAssociateAssessmentReportEvidenceResponse = {}  # type: ignore[typeddict-item]
    if "evidenceIds" in data:
        import capo_auditmanager.types.evidence_ids

        out["evidence_ids"] = capo_auditmanager.types.evidence_ids.deserialize_json(
            data["evidenceIds"]
        )
    if "errors" in data:
        import capo_auditmanager.types.assessment_report_evidence_errors

        out["errors"] = (
            capo_auditmanager.types.assessment_report_evidence_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
