"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDisassociateAssessmentReportEvidenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.evidence_ids
    import aws_sdk_auditmanager.types.uuid


class BatchDisassociateAssessmentReportEvidenceRequest(TypedDict, closed=True):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    evidence_folder_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the folder that the evidence is stored in. </p>"""
    evidence_ids: "aws_sdk_auditmanager.types.evidence_ids.EvidenceIds"
    """<p> The list of evidence identifiers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateAssessmentReportEvidenceRequest) -> dict:
    out: dict = {}
    out["evidenceFolderId"] = value["evidence_folder_id"]
    import aws_sdk_auditmanager.types.evidence_ids

    out["evidenceIds"] = aws_sdk_auditmanager.types.evidence_ids.serialize_json(
        value["evidence_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDisassociateAssessmentReportEvidenceRequest:
    out: BatchDisassociateAssessmentReportEvidenceRequest = {}  # type: ignore[typeddict-item]
    if "evidenceFolderId" in data:
        out["evidence_folder_id"] = data["evidenceFolderId"]
    else:
        raise DeserializationError(
            "BatchDisassociateAssessmentReportEvidenceRequest.evidence_folder_id required"
        )
    if "evidenceIds" in data:
        import aws_sdk_auditmanager.types.evidence_ids

        out["evidence_ids"] = aws_sdk_auditmanager.types.evidence_ids.deserialize_json(
            data["evidenceIds"]
        )
    else:
        raise DeserializationError(
            "BatchDisassociateAssessmentReportEvidenceRequest.evidence_ids required"
        )
    return out
