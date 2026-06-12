"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentValidations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_validation

AssessmentValidations: TypeAlias = list[
    "aws_sdk_directory_service.types.assessment_validation.AssessmentValidation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentValidations) -> list:
    import aws_sdk_directory_service.types.assessment_validation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.assessment_validation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentValidations:
    import aws_sdk_directory_service.types.assessment_validation

    out: AssessmentValidations = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.assessment_validation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
