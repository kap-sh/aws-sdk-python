"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CancelTaskInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.task_id

class CancelTaskInput(TypedDict):
    task_id: "aws_sdk_snow_device_management.types.task_id.TaskId"
    """<p>The ID of the task that you are attempting to cancel. You can retrieve a task ID by using the <code>ListTasks</code> operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CancelTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelTaskInput:
    out: CancelTaskInput = {}  # type: ignore[typeddict-item]
    return out