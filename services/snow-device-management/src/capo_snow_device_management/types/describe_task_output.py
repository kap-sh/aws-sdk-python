"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_snow_device_management.types.tag_map
    import capo_snow_device_management.types.target_list
    import capo_snow_device_management.types.task_description_string
    import capo_snow_device_management.types.task_state


class DescribeTaskOutput(TypedDict, closed=True):
    task_id: NotRequired["str"]
    """<p>The ID of the task.</p>"""
    task_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    targets: NotRequired["capo_snow_device_management.types.target_list.TargetList"]
    """<p>The managed devices that the task was sent to.</p>"""
    state: NotRequired["capo_snow_device_management.types.task_state.TaskState"]
    """<p>The current state of the task.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>When the <code>CreateTask</code> operation was called.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>When the state of the task was last updated.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>When the task was completed.</p>"""
    description: NotRequired[
        "capo_snow_device_management.types.task_description_string.TaskDescriptionString"
    ]
    """<p>The description provided of the task and managed devices.</p>"""
    tags: NotRequired["capo_snow_device_management.types.tag_map.TagMap"]
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTaskOutput) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "targets" in value:
        import capo_snow_device_management.types.target_list

        out["targets"] = capo_snow_device_management.types.target_list.serialize_json(
            value["targets"]
        )
    if "state" in value:
        out["state"] = value["state"]
    if "created_at" in value:
        import capo_snow_device_management.types._prelude.timestamp

        out["createdAt"] = (
            capo_snow_device_management.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_snow_device_management.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            capo_snow_device_management.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "completed_at" in value:
        import capo_snow_device_management.types._prelude.timestamp

        out["completedAt"] = (
            capo_snow_device_management.types._prelude.timestamp.serialize_json(
                value["completed_at"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_snow_device_management.types.tag_map

        out["tags"] = capo_snow_device_management.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribeTaskOutput:
    out: DescribeTaskOutput = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    if "targets" in data:
        import capo_snow_device_management.types.target_list

        out["targets"] = capo_snow_device_management.types.target_list.deserialize_json(
            data["targets"]
        )
    if "state" in data:
        out["state"] = data["state"]
    if "createdAt" in data:
        import capo_snow_device_management.types._prelude.timestamp

        out["created_at"] = (
            capo_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import capo_snow_device_management.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "completedAt" in data:
        import capo_snow_device_management.types._prelude.timestamp

        out["completed_at"] = (
            capo_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["completedAt"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_snow_device_management.types.tag_map

        out["tags"] = capo_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
