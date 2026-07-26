"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFolderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_evidence_folder


class GetEvidenceFolderResponse(TypedDict, closed=True):
    evidence_folder: NotRequired[
        "capo_auditmanager.types.assessment_evidence_folder.AssessmentEvidenceFolder"
    ]
    """<p> The folder that the evidence is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFolderResponse) -> dict:
    out: dict = {}
    if "evidence_folder" in value:
        import capo_auditmanager.types.assessment_evidence_folder

        out["evidenceFolder"] = (
            capo_auditmanager.types.assessment_evidence_folder.serialize_json(
                value["evidence_folder"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEvidenceFolderResponse:
    out: GetEvidenceFolderResponse = {}  # type: ignore[typeddict-item]
    if "evidenceFolder" in data:
        import capo_auditmanager.types.assessment_evidence_folder

        out["evidence_folder"] = (
            capo_auditmanager.types.assessment_evidence_folder.deserialize_json(
                data["evidenceFolder"]
            )
        )
    return out
