"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.command_parameter_name
    import capo_iot.types.command_parameter_value

CommandExecutionParameterMap: TypeAlias = dict[
    "capo_iot.types.command_parameter_name.CommandParameterName",
    "capo_iot.types.command_parameter_value.CommandParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CommandExecutionParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iot.types.command_parameter_value

        out[key] = capo_iot.types.command_parameter_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CommandExecutionParameterMap:
    out: CommandExecutionParameterMap = {}
    for key, value in data.items():
        import capo_iot.types.command_parameter_value

        out[key] = capo_iot.types.command_parameter_value.deserialize_json(value)
    return out
