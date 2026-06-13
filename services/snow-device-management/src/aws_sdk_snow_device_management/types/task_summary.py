"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#TaskSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_snow_device_management.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.tag_map
    import aws_sdk_snow_device_management.types.task_id
    import aws_sdk_snow_device_management.types.task_state


class TaskSummary(TypedDict):
    task_id: "aws_sdk_snow_device_management.types.task_id.TaskId"
    """<p>The task ID.</p>"""
    task_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    state: NotRequired["aws_sdk_snow_device_management.types.task_state.TaskState"]
    """<p>The state of the task assigned to one or many devices.</p>"""
    tags: NotRequired["aws_sdk_snow_device_management.types.tag_map.TagMap"]
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummary) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "state" in value:
        out["state"] = value["state"]
    if "tags" in value:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TaskSummary:
    out: TaskSummary = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("TaskSummary.task_id required")
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    if "state" in data:
        out["state"] = data["state"]
    if "tags" in data:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
