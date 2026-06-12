"""Generated from Smithy shape ``com.amazonaws.ssm#CommandPluginList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.command_plugin

CommandPluginList: TypeAlias = list["aws_sdk_ssm.types.command_plugin.CommandPlugin"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandPluginList) -> list:
    import aws_sdk_ssm.types.command_plugin

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.command_plugin.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandPluginList:
    import aws_sdk_ssm.types.command_plugin

    out: CommandPluginList = []
    for item in data:
        out.append(aws_sdk_ssm.types.command_plugin.deserialize_aws_json_1_1(item))
    return out
