"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionResultMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.command_execution_result
    import capo_iot.types.command_execution_result_name

CommandExecutionResultMap: TypeAlias = dict[
    "capo_iot.types.command_execution_result_name.CommandExecutionResultName",
    "capo_iot.types.command_execution_result.CommandExecutionResult",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CommandExecutionResultMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iot.types.command_execution_result

        out[key] = capo_iot.types.command_execution_result.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CommandExecutionResultMap:
    out: CommandExecutionResultMap = {}
    for key, value in data.items():
        import capo_iot.types.command_execution_result

        out[key] = capo_iot.types.command_execution_result.deserialize_json(value)
    return out
