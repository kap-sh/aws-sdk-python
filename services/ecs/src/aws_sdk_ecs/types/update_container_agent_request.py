"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerAgentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class UpdateContainerAgentRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container_instance: "aws_sdk_ecs.types.string.String"
    """<p>The container instance ID or full ARN entries for the container instance where you would like to update the Amazon ECS container agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerAgentRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    out["containerInstance"] = value["container_instance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerAgentRequest:
    out: UpdateContainerAgentRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "containerInstance" in data:
        out["container_instance"] = data["containerInstance"]
    else:
        raise DeserializationError(
            "UpdateContainerAgentRequest.container_instance required"
        )
    return out
