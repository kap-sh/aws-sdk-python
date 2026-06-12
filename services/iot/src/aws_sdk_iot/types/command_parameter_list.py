"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_parameter

CommandParameterList: TypeAlias = list[
    "aws_sdk_iot.types.command_parameter.CommandParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterList) -> list:
    import aws_sdk_iot.types.command_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.command_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CommandParameterList:
    import aws_sdk_iot.types.command_parameter

    out: CommandParameterList = []
    for item in data:
        out.append(aws_sdk_iot.types.command_parameter.deserialize_json(item))
    return out
