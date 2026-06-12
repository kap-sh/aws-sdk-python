"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_set_id
    import aws_sdk_auditmanager.types.manual_evidence_list
    import aws_sdk_auditmanager.types.uuid


class BatchImportEvidenceToAssessmentControlRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    control_set_id: "aws_sdk_auditmanager.types.control_set_id.ControlSetId"
    """<p> The identifier for the control set. </p>"""
    control_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the control. </p>"""
    manual_evidence: (
        "aws_sdk_auditmanager.types.manual_evidence_list.ManualEvidenceList"
    )
    """<p> The list of manual evidence objects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlRequest) -> dict:
    out: dict = {}
    import aws_sdk_auditmanager.types.manual_evidence_list

    out["manualEvidence"] = (
        aws_sdk_auditmanager.types.manual_evidence_list.serialize_json(
            value["manual_evidence"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchImportEvidenceToAssessmentControlRequest:
    out: BatchImportEvidenceToAssessmentControlRequest = {}  # type: ignore[typeddict-item]
    if "manualEvidence" in data:
        import aws_sdk_auditmanager.types.manual_evidence_list

        out["manual_evidence"] = (
            aws_sdk_auditmanager.types.manual_evidence_list.deserialize_json(
                data["manualEvidence"]
            )
        )
    else:
        raise DeserializationError(
            "BatchImportEvidenceToAssessmentControlRequest.manual_evidence required"
        )
    return out
