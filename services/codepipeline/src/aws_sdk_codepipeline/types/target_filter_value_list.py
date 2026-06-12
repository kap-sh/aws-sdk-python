"""Generated from Smithy shape ``com.amazonaws.codepipeline#TargetFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.target_filter_value

TargetFilterValueList: TypeAlias = list[
    "aws_sdk_codepipeline.types.target_filter_value.TargetFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetFilterValueList:
    return list(data)
