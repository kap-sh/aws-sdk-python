"""Generated from Smithy shape ``com.amazonaws.auditmanager#DisassociateAssessmentReportEvidenceFolderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class DisassociateAssessmentReportEvidenceFolderRequest(TypedDict, closed=True):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    evidence_folder_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the folder that the evidence is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAssessmentReportEvidenceFolderRequest) -> dict:
    out: dict = {}
    out["evidenceFolderId"] = value["evidence_folder_id"]
    return out


def deserialize_json(data: dict) -> DisassociateAssessmentReportEvidenceFolderRequest:
    out: DisassociateAssessmentReportEvidenceFolderRequest = {}  # type: ignore[typeddict-item]
    if "evidenceFolderId" in data:
        out["evidence_folder_id"] = data["evidenceFolderId"]
    else:
        raise DeserializationError(
            "DisassociateAssessmentReportEvidenceFolderRequest.evidence_folder_id required"
        )
    return out
