"""Generated from Smithy shape ``com.amazonaws.ssm#CommandPluginList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.command_plugin

CommandPluginList: TypeAlias = list["capo_ssm.types.command_plugin.CommandPlugin"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandPluginList) -> list:
    import capo_ssm.types.command_plugin

    out: list = []
    for item in value:
        out.append(capo_ssm.types.command_plugin.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandPluginList:
    import capo_ssm.types.command_plugin

    out: CommandPluginList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.command_plugin.deserialize_aws_json_1_1(item))
    return out
