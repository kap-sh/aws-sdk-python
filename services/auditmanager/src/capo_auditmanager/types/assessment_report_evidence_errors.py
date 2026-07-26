"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportEvidenceErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_report_evidence_error

AssessmentReportEvidenceErrors: TypeAlias = list[
    "capo_auditmanager.types.assessment_report_evidence_error.AssessmentReportEvidenceError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportEvidenceErrors) -> list:
    import capo_auditmanager.types.assessment_report_evidence_error

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.assessment_report_evidence_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssessmentReportEvidenceErrors:
    import capo_auditmanager.types.assessment_report_evidence_error

    out: AssessmentReportEvidenceErrors = []
    for item in data:
        out.append(
            capo_auditmanager.types.assessment_report_evidence_error.deserialize_json(
                item
            )
        )
    return out
