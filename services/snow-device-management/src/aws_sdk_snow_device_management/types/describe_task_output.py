"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeTaskOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_snow_device_management.types.tag_map
    import aws_sdk_snow_device_management.types.target_list
    import aws_sdk_snow_device_management.types.task_description_string
    import aws_sdk_snow_device_management.types.task_state


class DescribeTaskOutput(TypedDict):
    task_id: NotRequired["str"]
    """<p>The ID of the task.</p>"""
    task_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    targets: NotRequired["aws_sdk_snow_device_management.types.target_list.TargetList"]
    """<p>The managed devices that the task was sent to.</p>"""
    state: NotRequired["aws_sdk_snow_device_management.types.task_state.TaskState"]
    """<p>The current state of the task.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>When the <code>CreateTask</code> operation was called.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>When the state of the task was last updated.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>When the task was completed.</p>"""
    description: NotRequired[
        "aws_sdk_snow_device_management.types.task_description_string.TaskDescriptionString"
    ]
    """<p>The description provided of the task and managed devices.</p>"""
    tags: NotRequired["aws_sdk_snow_device_management.types.tag_map.TagMap"]
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTaskOutput) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "targets" in value:
        import aws_sdk_snow_device_management.types.target_list

        out["targets"] = (
            aws_sdk_snow_device_management.types.target_list.serialize_json(
                value["targets"]
            )
        )
    if "state" in value:
        out["state"] = value["state"]
    if "created_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "completed_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["completedAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["completed_at"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.serialize_json(
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
        import aws_sdk_snow_device_management.types.target_list

        out["targets"] = (
            aws_sdk_snow_device_management.types.target_list.deserialize_json(
                data["targets"]
            )
        )
    if "state" in data:
        out["state"] = data["state"]
    if "createdAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "completedAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["completed_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["completedAt"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
