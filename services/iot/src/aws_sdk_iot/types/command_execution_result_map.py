"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionResultMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_execution_result
    import aws_sdk_iot.types.command_execution_result_name

CommandExecutionResultMap: TypeAlias = dict[
    "aws_sdk_iot.types.command_execution_result_name.CommandExecutionResultName",
    "aws_sdk_iot.types.command_execution_result.CommandExecutionResult",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CommandExecutionResultMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iot.types.command_execution_result

        out[key] = aws_sdk_iot.types.command_execution_result.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CommandExecutionResultMap:
    out: CommandExecutionResultMap = {}
    for key, value in data.items():
        import aws_sdk_iot.types.command_execution_result

        out[key] = aws_sdk_iot.types.command_execution_result.deserialize_json(value)
    return out
