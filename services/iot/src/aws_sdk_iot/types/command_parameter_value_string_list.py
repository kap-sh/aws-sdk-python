"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.string_parameter_value

CommandParameterValueStringList: TypeAlias = list[
    "aws_sdk_iot.types.string_parameter_value.StringParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> CommandParameterValueStringList:
    return list(data)
