"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentStopEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.command_execution_status


class ContentStopEvent(TypedDict, closed=True):
    exit_code: "int"
    """<p>The exit code returned by the executed command. An exit code of 0 indicates successful execution, -1 indicates a platform error, and values greater than 0 indicate command-specific errors.</p>"""
    status: (
        "capo_bedrock_agentcore.types.command_execution_status.CommandExecutionStatus"
    )
    """<p>The final status of the command execution. Valid values are <code>COMPLETED</code> for successful completion or <code>TIMED_OUT</code> if the command exceeded the specified timeout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentStopEvent) -> dict:
    out: dict = {}
    out["exitCode"] = value["exit_code"]
    import capo_bedrock_agentcore.types.command_execution_status

    out["status"] = (
        capo_bedrock_agentcore.types.command_execution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContentStopEvent:
    out: ContentStopEvent = {}  # type: ignore[typeddict-item]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    else:
        raise DeserializationError("ContentStopEvent.exit_code required")
    if "status" in data:
        import capo_bedrock_agentcore.types.command_execution_status

        out["status"] = (
            capo_bedrock_agentcore.types.command_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ContentStopEvent.status required")
    return out
