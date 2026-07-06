"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDisassociateAssessmentReportEvidenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_report_evidence_errors
    import aws_sdk_auditmanager.types.evidence_ids


class BatchDisassociateAssessmentReportEvidenceResponse(TypedDict, closed=True):
    evidence_ids: NotRequired["aws_sdk_auditmanager.types.evidence_ids.EvidenceIds"]
    """<p> The identifier for the evidence. </p>"""
    errors: NotRequired[
        "aws_sdk_auditmanager.types.assessment_report_evidence_errors.AssessmentReportEvidenceErrors"
    ]
    """<p> A list of errors that the <code>BatchDisassociateAssessmentReportEvidence</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateAssessmentReportEvidenceResponse) -> dict:
    out: dict = {}
    if "evidence_ids" in value:
        import aws_sdk_auditmanager.types.evidence_ids

        out["evidenceIds"] = aws_sdk_auditmanager.types.evidence_ids.serialize_json(
            value["evidence_ids"]
        )
    if "errors" in value:
        import aws_sdk_auditmanager.types.assessment_report_evidence_errors

        out["errors"] = (
            aws_sdk_auditmanager.types.assessment_report_evidence_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDisassociateAssessmentReportEvidenceResponse:
    out: BatchDisassociateAssessmentReportEvidenceResponse = {}  # type: ignore[typeddict-item]
    if "evidenceIds" in data:
        import aws_sdk_auditmanager.types.evidence_ids

        out["evidence_ids"] = aws_sdk_auditmanager.types.evidence_ids.deserialize_json(
            data["evidenceIds"]
        )
    if "errors" in data:
        import aws_sdk_auditmanager.types.assessment_report_evidence_errors

        out["errors"] = (
            aws_sdk_auditmanager.types.assessment_report_evidence_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
