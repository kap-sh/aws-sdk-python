"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFolderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_evidence_folder


class GetEvidenceFolderResponse(TypedDict, closed=True):
    evidence_folder: NotRequired[
        "aws_sdk_auditmanager.types.assessment_evidence_folder.AssessmentEvidenceFolder"
    ]
    """<p> The folder that the evidence is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFolderResponse) -> dict:
    out: dict = {}
    if "evidence_folder" in value:
        import aws_sdk_auditmanager.types.assessment_evidence_folder

        out["evidenceFolder"] = (
            aws_sdk_auditmanager.types.assessment_evidence_folder.serialize_json(
                value["evidence_folder"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEvidenceFolderResponse:
    out: GetEvidenceFolderResponse = {}  # type: ignore[typeddict-item]
    if "evidenceFolder" in data:
        import aws_sdk_auditmanager.types.assessment_evidence_folder

        out["evidence_folder"] = (
            aws_sdk_auditmanager.types.assessment_evidence_folder.deserialize_json(
                data["evidenceFolder"]
            )
        )
    return out
