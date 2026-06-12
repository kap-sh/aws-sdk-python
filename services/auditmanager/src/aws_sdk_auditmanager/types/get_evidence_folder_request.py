"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFolderRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_set_id
    import aws_sdk_auditmanager.types.uuid


class GetEvidenceFolderRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    control_set_id: "aws_sdk_auditmanager.types.control_set_id.ControlSetId"
    """<p> The unique identifier for the control set. </p>"""
    evidence_folder_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the folder that the evidence is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFolderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvidenceFolderRequest:
    out: GetEvidenceFolderRequest = {}  # type: ignore[typeddict-item]
    return out
