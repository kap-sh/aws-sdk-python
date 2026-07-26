"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.command_arn
    import capo_iot.types.command_execution_id
    import capo_iot.types.command_execution_status
    import capo_iot.types.date_type
    import capo_iot.types.target_arn


class CommandExecutionSummary(TypedDict, closed=True):
    command_arn: NotRequired["capo_iot.types.command_arn.CommandArn"]
    """<p>The Amazon Resource Name (ARN) of the command execution.</p>"""
    execution_id: NotRequired["capo_iot.types.command_execution_id.CommandExecutionId"]
    """<p>The unique identifier of the command execution.</p>"""
    target_arn: NotRequired["capo_iot.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Name (ARN) of the target device for which the command is being executed.</p>"""
    status: NotRequired[
        "capo_iot.types.command_execution_status.CommandExecutionStatus"
    ]
    """<p>The status of the command executions.</p>"""
    created_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date and time at which the command execution was created for the target device.</p>"""
    started_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date and time at which the command started executing on the target device.</p>"""
    completed_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date and time at which the command completed executing on the target device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandExecutionSummary) -> dict:
    out: dict = {}
    if "command_arn" in value:
        out["commandArn"] = value["command_arn"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import capo_iot.types.command_execution_status

        out["status"] = capo_iot.types.command_execution_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_iot.types.date_type

        out["createdAt"] = capo_iot.types.date_type.serialize_json(value["created_at"])
    if "started_at" in value:
        import capo_iot.types.date_type

        out["startedAt"] = capo_iot.types.date_type.serialize_json(value["started_at"])
    if "completed_at" in value:
        import capo_iot.types.date_type

        out["completedAt"] = capo_iot.types.date_type.serialize_json(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> CommandExecutionSummary:
    out: CommandExecutionSummary = {}  # type: ignore[typeddict-item]
    if "commandArn" in data:
        out["command_arn"] = data["commandArn"]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "status" in data:
        import capo_iot.types.command_execution_status

        out["status"] = capo_iot.types.command_execution_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import capo_iot.types.date_type

        out["created_at"] = capo_iot.types.date_type.deserialize_json(data["createdAt"])
    if "startedAt" in data:
        import capo_iot.types.date_type

        out["started_at"] = capo_iot.types.date_type.deserialize_json(data["startedAt"])
    if "completedAt" in data:
        import capo_iot.types.date_type

        out["completed_at"] = capo_iot.types.date_type.deserialize_json(
            data["completedAt"]
        )
    return out
