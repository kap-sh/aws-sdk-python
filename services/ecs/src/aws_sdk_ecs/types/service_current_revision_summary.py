"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceCurrentRevisionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string


class ServiceCurrentRevisionSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the current service revision.</p>"""
    requested_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of requested tasks in the current service revision</p>"""
    running_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of running tasks of the current service revision</p>"""
    pending_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of pending tasks in the current service revision</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceCurrentRevisionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    out["requestedTaskCount"] = value.get("requested_task_count", 0)
    out["runningTaskCount"] = value.get("running_task_count", 0)
    out["pendingTaskCount"] = value.get("pending_task_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceCurrentRevisionSummary:
    out: ServiceCurrentRevisionSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "requestedTaskCount" in data:
        out["requested_task_count"] = data["requestedTaskCount"]
    else:
        out["requested_task_count"] = 0
    if "runningTaskCount" in data:
        out["running_task_count"] = data["runningTaskCount"]
    else:
        out["running_task_count"] = 0
    if "pendingTaskCount" in data:
        out["pending_task_count"] = data["pendingTaskCount"]
    else:
        out["pending_task_count"] = 0
    return out
