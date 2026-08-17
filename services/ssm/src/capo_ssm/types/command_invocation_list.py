"""Generated from Smithy shape ``com.amazonaws.ssm#CommandInvocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.command_invocation

CommandInvocationList: TypeAlias = list[
    "capo_ssm.types.command_invocation.CommandInvocation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandInvocationList) -> list:
    import capo_ssm.types.command_invocation

    out: list = []
    for item in value:
        out.append(capo_ssm.types.command_invocation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandInvocationList:
    import capo_ssm.types.command_invocation

    out: CommandInvocationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.command_invocation.deserialize_aws_json_1_1(item))
    return out
