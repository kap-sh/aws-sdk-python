"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.condition

ConditionList: TypeAlias = list["aws_sdk_codepipeline.types.condition.Condition"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionList) -> list:
    import aws_sdk_codepipeline.types.condition

    out: list = []
    for item in value:
        out.append(aws_sdk_codepipeline.types.condition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConditionList:
    import aws_sdk_codepipeline.types.condition

    out: ConditionList = []
    for item in data:
        out.append(aws_sdk_codepipeline.types.condition.deserialize_aws_json_1_1(item))
    return out
