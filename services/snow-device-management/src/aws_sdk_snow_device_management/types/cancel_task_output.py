"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CancelTaskOutput``."""

from typing_extensions import NotRequired, TypedDict


class CancelTaskOutput(TypedDict, closed=True):
    task_id: NotRequired["str"]
    """<p>The ID of the task that you are attempting to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelTaskOutput) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> CancelTaskOutput:
    out: CancelTaskOutput = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    return out
