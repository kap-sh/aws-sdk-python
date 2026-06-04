"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskSetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.scale
    import aws_sdk_ecs.types.string


class UpdateTaskSetRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set is found in.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task set is found in.</p>"""
    task_set: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the task set to update.</p>"""
    scale: "aws_sdk_ecs.types.scale.Scale"
    """<p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskSetRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    out["taskSet"] = value["task_set"]
    import aws_sdk_ecs.types.scale

    out["scale"] = aws_sdk_ecs.types.scale.serialize_aws_json_1_1(value["scale"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskSetRequest:
    out: UpdateTaskSetRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError("UpdateTaskSetRequest.cluster required")
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("UpdateTaskSetRequest.service required")
    if "taskSet" in data:
        out["task_set"] = data["taskSet"]
    else:
        raise DeserializationError("UpdateTaskSetRequest.task_set required")
    if "scale" in data:
        import aws_sdk_ecs.types.scale

        out["scale"] = aws_sdk_ecs.types.scale.deserialize_aws_json_1_1(data["scale"])
    else:
        raise DeserializationError("UpdateTaskSetRequest.scale required")
    return out
