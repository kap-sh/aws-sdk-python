"""Generated from Smithy shape ``com.amazonaws.codebuild#ComputeTypesAllowed``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string

ComputeTypesAllowed: TypeAlias = list[
    "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeTypesAllowed) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ComputeTypesAllowed:
    return list(data)
