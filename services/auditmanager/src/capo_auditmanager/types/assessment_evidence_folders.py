"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentEvidenceFolders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_evidence_folder

AssessmentEvidenceFolders: TypeAlias = list[
    "capo_auditmanager.types.assessment_evidence_folder.AssessmentEvidenceFolder"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentEvidenceFolders) -> list:
    import capo_auditmanager.types.assessment_evidence_folder

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.assessment_evidence_folder.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssessmentEvidenceFolders:
    import capo_auditmanager.types.assessment_evidence_folder

    out: AssessmentEvidenceFolders = []
    for item in data:
        out.append(
            capo_auditmanager.types.assessment_evidence_folder.deserialize_json(item)
        )
    return out
