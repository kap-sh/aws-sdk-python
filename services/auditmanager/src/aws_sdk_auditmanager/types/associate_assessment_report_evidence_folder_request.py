"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssociateAssessmentReportEvidenceFolderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class AssociateAssessmentReportEvidenceFolderRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    evidence_folder_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the folder that the evidence is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAssessmentReportEvidenceFolderRequest) -> dict:
    out: dict = {}
    out["evidenceFolderId"] = value["evidence_folder_id"]
    return out


def deserialize_json(data: dict) -> AssociateAssessmentReportEvidenceFolderRequest:
    out: AssociateAssessmentReportEvidenceFolderRequest = {}  # type: ignore[typeddict-item]
    if "evidenceFolderId" in data:
        out["evidence_folder_id"] = data["evidenceFolderId"]
    else:
        raise DeserializationError(
            "AssociateAssessmentReportEvidenceFolderRequest.evidence_folder_id required"
        )
    return out
