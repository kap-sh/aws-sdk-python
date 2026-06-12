"""Generated from Smithy shape ``com.amazonaws.ssm#CommandFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.command_filter

CommandFilterList: TypeAlias = list["aws_sdk_ssm.types.command_filter.CommandFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandFilterList) -> list:
    import aws_sdk_ssm.types.command_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.command_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandFilterList:
    import aws_sdk_ssm.types.command_filter

    out: CommandFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.command_filter.deserialize_aws_json_1_1(item))
    return out
