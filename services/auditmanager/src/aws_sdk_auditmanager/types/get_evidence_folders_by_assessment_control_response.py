"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFoldersByAssessmentControlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_evidence_folders
    import aws_sdk_auditmanager.types.token


class GetEvidenceFoldersByAssessmentControlResponse(TypedDict, closed=True):
    evidence_folders: NotRequired[
        "aws_sdk_auditmanager.types.assessment_evidence_folders.AssessmentEvidenceFolders"
    ]
    """<p> The list of evidence folders that the <code>GetEvidenceFoldersByAssessmentControl</code> API returned. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFoldersByAssessmentControlResponse) -> dict:
    out: dict = {}
    if "evidence_folders" in value:
        import aws_sdk_auditmanager.types.assessment_evidence_folders

        out["evidenceFolders"] = (
            aws_sdk_auditmanager.types.assessment_evidence_folders.serialize_json(
                value["evidence_folders"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEvidenceFoldersByAssessmentControlResponse:
    out: GetEvidenceFoldersByAssessmentControlResponse = {}  # type: ignore[typeddict-item]
    if "evidenceFolders" in data:
        import aws_sdk_auditmanager.types.assessment_evidence_folders

        out["evidence_folders"] = (
            aws_sdk_auditmanager.types.assessment_evidence_folders.deserialize_json(
                data["evidenceFolders"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
