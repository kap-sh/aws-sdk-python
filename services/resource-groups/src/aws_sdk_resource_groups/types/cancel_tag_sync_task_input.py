"""Generated from Smithy shape ``com.amazonaws.resourcegroups#CancelTagSyncTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.tag_sync_task_arn


class CancelTagSyncTaskInput(TypedDict):
    task_arn: "aws_sdk_resource_groups.types.tag_sync_task_arn.TagSyncTaskArn"
    """<p>The Amazon resource name (ARN) of the tag-sync task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelTagSyncTaskInput) -> dict:
    out: dict = {}
    out["TaskArn"] = value["task_arn"]
    return out


def deserialize_json(data: dict) -> CancelTagSyncTaskInput:
    out: CancelTagSyncTaskInput = {}  # type: ignore[typeddict-item]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    else:
        raise DeserializationError("CancelTagSyncTaskInput.task_arn required")
    return out
