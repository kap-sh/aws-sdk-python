"""Generated from Smithy shape ``com.amazonaws.codebuild#CommandExecutions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.command_execution

CommandExecutions: TypeAlias = list[
    "aws_sdk_codebuild.types.command_execution.CommandExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandExecutions) -> list:
    import aws_sdk_codebuild.types.command_execution

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.command_execution.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CommandExecutions:
    import aws_sdk_codebuild.types.command_execution

    out: CommandExecutions = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.command_execution.deserialize_aws_json_1_1(item)
        )
    return out
