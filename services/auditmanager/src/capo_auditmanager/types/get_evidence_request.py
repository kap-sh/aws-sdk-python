"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.uuid


class GetEvidenceRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId"
    """<p> The unique identifier for the control set. </p>"""
    evidence_folder_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the folder that the evidence is stored in. </p>"""
    evidence_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the evidence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvidenceRequest:
    out: GetEvidenceRequest = {}  # type: ignore[typeddict-item]
    return out
