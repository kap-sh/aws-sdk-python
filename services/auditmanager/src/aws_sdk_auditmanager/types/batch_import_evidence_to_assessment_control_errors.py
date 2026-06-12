"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.batch_import_evidence_to_assessment_control_error

BatchImportEvidenceToAssessmentControlErrors: TypeAlias = list[
    "aws_sdk_auditmanager.types.batch_import_evidence_to_assessment_control_error.BatchImportEvidenceToAssessmentControlError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlErrors) -> list:
    import aws_sdk_auditmanager.types.batch_import_evidence_to_assessment_control_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.batch_import_evidence_to_assessment_control_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchImportEvidenceToAssessmentControlErrors:
    import aws_sdk_auditmanager.types.batch_import_evidence_to_assessment_control_error

    out: BatchImportEvidenceToAssessmentControlErrors = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.batch_import_evidence_to_assessment_control_error.deserialize_json(
                item
            )
        )
    return out
