"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportsMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_report_metadata

AssessmentReportsMetadata: TypeAlias = list[
    "aws_sdk_auditmanager.types.assessment_report_metadata.AssessmentReportMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportsMetadata) -> list:
    import aws_sdk_auditmanager.types.assessment_report_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.assessment_report_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssessmentReportsMetadata:
    import aws_sdk_auditmanager.types.assessment_report_metadata

    out: AssessmentReportsMetadata = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.assessment_report_metadata.deserialize_json(item)
        )
    return out
