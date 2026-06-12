"""Generated from Smithy shape ``com.amazonaws.directoryservice#Assessments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_summary

Assessments: TypeAlias = list[
    "aws_sdk_directory_service.types.assessment_summary.AssessmentSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Assessments) -> list:
    import aws_sdk_directory_service.types.assessment_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.assessment_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Assessments:
    import aws_sdk_directory_service.types.assessment_summary

    out: Assessments = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.assessment_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
