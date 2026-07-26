"""Generated from Smithy shape ``com.amazonaws.codepipeline#CommandList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.command

CommandList: TypeAlias = list["capo_codepipeline.types.command.Command"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CommandList:
    return list(data)
