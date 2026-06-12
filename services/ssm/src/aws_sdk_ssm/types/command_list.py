"""Generated from Smithy shape ``com.amazonaws.ssm#CommandList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.command

CommandList: TypeAlias = list["aws_sdk_ssm.types.command.Command"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandList) -> list:
    import aws_sdk_ssm.types.command

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.command.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandList:
    import aws_sdk_ssm.types.command

    out: CommandList = []
    for item in data:
        out.append(aws_sdk_ssm.types.command.deserialize_aws_json_1_1(item))
    return out
