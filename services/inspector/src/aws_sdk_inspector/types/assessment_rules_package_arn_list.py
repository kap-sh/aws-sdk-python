"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRulesPackageArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn

AssessmentRulesPackageArnList: TypeAlias = list["aws_sdk_inspector.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRulesPackageArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AssessmentRulesPackageArnList:
    return list(data)
