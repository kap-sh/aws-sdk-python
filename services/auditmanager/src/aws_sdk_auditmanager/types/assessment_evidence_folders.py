"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentEvidenceFolders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_evidence_folder

AssessmentEvidenceFolders: TypeAlias = list[
    "aws_sdk_auditmanager.types.assessment_evidence_folder.AssessmentEvidenceFolder"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentEvidenceFolders) -> list:
    import aws_sdk_auditmanager.types.assessment_evidence_folder

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.assessment_evidence_folder.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssessmentEvidenceFolders:
    import aws_sdk_auditmanager.types.assessment_evidence_folder

    out: AssessmentEvidenceFolders = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.assessment_evidence_folder.deserialize_json(item)
        )
    return out
