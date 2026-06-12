"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentInstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_instance_id

AssessmentInstanceIds: TypeAlias = list[
    "aws_sdk_directory_service.types.assessment_instance_id.AssessmentInstanceId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentInstanceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AssessmentInstanceIds:
    return list(data)
