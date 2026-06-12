"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CreateTaskOutput``."""

from typing import TypedDict
from typing_extensions import NotRequired

class CreateTaskOutput(TypedDict):
    task_id: NotRequired["str"]
    """<p>The ID of the task that you created.</p>"""
    task_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the task that you created.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateTaskOutput) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    return out


def deserialize_json(data: dict) -> CreateTaskOutput:
    out: CreateTaskOutput = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    return out