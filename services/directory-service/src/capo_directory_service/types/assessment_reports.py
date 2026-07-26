"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentReports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_report

AssessmentReports: TypeAlias = list[
    "capo_directory_service.types.assessment_report.AssessmentReport"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentReports) -> list:
    import capo_directory_service.types.assessment_report

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.assessment_report.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentReports:
    import capo_directory_service.types.assessment_report

    out: AssessmentReports = []
    for item in data:
        out.append(
            capo_directory_service.types.assessment_report.deserialize_aws_json_1_1(
                item
            )
        )
    return out
