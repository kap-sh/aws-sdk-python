"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.manual_evidence_list
    import capo_auditmanager.types.uuid


class BatchImportEvidenceToAssessmentControlRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId"
    """<p> The identifier for the control set. </p>"""
    control_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the control. </p>"""
    manual_evidence: "capo_auditmanager.types.manual_evidence_list.ManualEvidenceList"
    """<p> The list of manual evidence objects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlRequest) -> dict:
    out: dict = {}
    import capo_auditmanager.types.manual_evidence_list

    out["manualEvidence"] = capo_auditmanager.types.manual_evidence_list.serialize_json(
        value["manual_evidence"]
    )
    return out


def deserialize_json(data: dict) -> BatchImportEvidenceToAssessmentControlRequest:
    out: BatchImportEvidenceToAssessmentControlRequest = {}  # type: ignore[typeddict-item]
    if "manualEvidence" in data:
        import capo_auditmanager.types.manual_evidence_list

        out["manual_evidence"] = (
            capo_auditmanager.types.manual_evidence_list.deserialize_json(
                data["manualEvidence"]
            )
        )
    else:
        raise DeserializationError(
            "BatchImportEvidenceToAssessmentControlRequest.manual_evidence required"
        )
    return out
