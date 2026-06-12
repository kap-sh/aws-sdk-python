"""Generated from Smithy shape ``com.amazonaws.codebuild#CommandExecutionIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string

CommandExecutionIds: TypeAlias = list[
    "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandExecutionIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CommandExecutionIds:
    return list(data)
