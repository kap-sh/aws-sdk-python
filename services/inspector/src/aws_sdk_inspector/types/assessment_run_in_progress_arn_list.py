"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunInProgressArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn

AssessmentRunInProgressArnList: TypeAlias = list["aws_sdk_inspector.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunInProgressArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AssessmentRunInProgressArnList:
    return list(data)
