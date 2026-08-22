"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolResultStructuredContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.task_status


class ToolResultStructuredContent(TypedDict, closed=True):
    task_id: NotRequired["str"]
    """<p>The identifier of the task that produced the result.</p>"""
    task_status: NotRequired["capo_bedrock_agentcore.types.task_status.TaskStatus"]
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
        import capo_bedrock_agentcore.types.task_status

        out["taskStatus"] = capo_bedrock_agentcore.types.task_status.serialize_json(
            value["task_status"]
        )
    if "stdout" in value:
        out["stdout"] = value["stdout"]
    if "stderr" in value:
        out["stderr"] = value["stderr"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "execution_time" in value:
        out["executionTime"] = (
            "NaN"
            if value["execution_time"] != value["execution_time"]
            else "Infinity"
            if value["execution_time"] == float("inf")
            else "-Infinity"
            if value["execution_time"] == float("-inf")
            else value["execution_time"]
        )
    return out


def deserialize_json(data: dict) -> ToolResultStructuredContent:
    out: ToolResultStructuredContent = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("taskStatus") is not None:
        import capo_bedrock_agentcore.types.task_status

        out["task_status"] = capo_bedrock_agentcore.types.task_status.deserialize_json(
            data["taskStatus"]
        )
    if data.get("stdout") is not None:
        out["stdout"] = data["stdout"]
    if data.get("stderr") is not None:
        out["stderr"] = data["stderr"]
    if data.get("exitCode") is not None:
        out["exit_code"] = data["exitCode"]
    if data.get("executionTime") is not None:
        out["execution_time"] = float(data["executionTime"])
    return out
