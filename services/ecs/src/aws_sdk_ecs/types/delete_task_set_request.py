"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.string


class DeleteTaskSetRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set found in to delete.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.</p>"""
    task_set: "aws_sdk_ecs.types.string.String"
    """<p>The task set ID or full Amazon Resource Name (ARN) of the task set to delete.</p>"""
    force: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If <code>true</code>, you can delete a task set even if it hasn't been scaled down to zero.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTaskSetRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    out["taskSet"] = value["task_set"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTaskSetRequest:
    out: DeleteTaskSetRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError("DeleteTaskSetRequest.cluster required")
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("DeleteTaskSetRequest.service required")
    if "taskSet" in data:
        out["task_set"] = data["taskSet"]
    else:
        raise DeserializationError("DeleteTaskSetRequest.task_set required")
    if "force" in data:
        out["force"] = data["force"]
    return out
