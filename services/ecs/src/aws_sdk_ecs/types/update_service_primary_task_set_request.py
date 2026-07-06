"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateServicePrimaryTaskSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class UpdateServicePrimaryTaskSetRequest(TypedDict, closed=True):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.</p>"""
    primary_task_set: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServicePrimaryTaskSetRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    out["primaryTaskSet"] = value["primary_task_set"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServicePrimaryTaskSetRequest:
    out: UpdateServicePrimaryTaskSetRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError(
            "UpdateServicePrimaryTaskSetRequest.cluster required"
        )
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError(
            "UpdateServicePrimaryTaskSetRequest.service required"
        )
    if "primaryTaskSet" in data:
        out["primary_task_set"] = data["primaryTaskSet"]
    else:
        raise DeserializationError(
            "UpdateServicePrimaryTaskSetRequest.primary_task_set required"
        )
    return out
