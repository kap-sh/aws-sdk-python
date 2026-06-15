"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.binary_command_execution_result
    import aws_sdk_iot.types.boolean_command_execution_result
    import aws_sdk_iot.types.string_command_execution_result


class CommandExecutionResult(TypedDict):
    s: NotRequired[
        "aws_sdk_iot.types.string_command_execution_result.StringCommandExecutionResult"
    ]
    r"""<p>An attribute of type String. For example:</p> <p> <code>\"S\": \"Hello\"</code> </p>"""
    b: NotRequired[
        "aws_sdk_iot.types.boolean_command_execution_result.BooleanCommandExecutionResult"
    ]
    r"""<p>An attribute of type Boolean. For example:</p> <p> <code>\"BOOL\": true</code> </p>"""
    bin: NotRequired[
        "aws_sdk_iot.types.binary_command_execution_result.BinaryCommandExecutionResult"
    ]
    """<p>An attribute of type Binary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandExecutionResult) -> dict:
    out: dict = {}
    if "s" in value:
        out["S"] = value["s"]
    if "b" in value:
        out["B"] = value["b"]
    if "bin" in value:
        import aws_sdk_iot.types.binary_command_execution_result

        out["BIN"] = aws_sdk_iot.types.binary_command_execution_result.serialize_json(
            value["bin"]
        )
    return out


def deserialize_json(data: dict) -> CommandExecutionResult:
    out: CommandExecutionResult = {}  # type: ignore[typeddict-item]
    if "S" in data:
        out["s"] = data["S"]
    if "B" in data:
        out["b"] = data["B"]
    if "BIN" in data:
        import aws_sdk_iot.types.binary_command_execution_result

        out["bin"] = aws_sdk_iot.types.binary_command_execution_result.deserialize_json(
            data["BIN"]
        )
    return out
