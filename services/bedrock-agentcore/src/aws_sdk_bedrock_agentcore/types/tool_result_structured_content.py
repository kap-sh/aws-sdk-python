"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolResultStructuredContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.task_status


class ToolResultStructuredContent(TypedDict):
    task_id: NotRequired["str"]
    """<p>The identifier of the task that produced the result.</p>"""
    task_status: NotRequired["aws_sdk_bedrock_agentcore.types.task_status.TaskStatus"]
    """<p>The status of the task that produced the result.</p>"""
    stdout: NotRequired["str"]
    """<p>The standard output from the tool execution.</p>"""
    stderr: NotRequired["str"]
    """<p>The standard error output from the tool execution.</p>"""
    exit_code: NotRequired["int"]
    """<p>The exit code from the tool execution.</p>"""
    execution_time: NotRequired["float"]
    """<p>The execution time of the tool operation in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultStructuredContent) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_status" in value:
        import aws_sdk_bedrock_agentcore.types.task_status

        out["taskStatus"] = aws_sdk_bedrock_agentcore.types.task_status.serialize_json(
            value["task_status"]
        )
    if "stdout" in value:
        out["stdout"] = value["stdout"]
    if "stderr" in value:
        out["stderr"] = value["stderr"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "execution_time" in value:
        out["executionTime"] = value["execution_time"]
    return out


def deserialize_json(data: dict) -> ToolResultStructuredContent:
    out: ToolResultStructuredContent = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "taskStatus" in data:
        import aws_sdk_bedrock_agentcore.types.task_status

        out["task_status"] = (
            aws_sdk_bedrock_agentcore.types.task_status.deserialize_json(
                data["taskStatus"]
            )
        )
    if "stdout" in data:
        out["stdout"] = data["stdout"]
    if "stderr" in data:
        out["stderr"] = data["stderr"]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "executionTime" in data:
        out["execution_time"] = data["executionTime"]
    return out
