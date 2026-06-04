"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerInstancesStateRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class UpdateContainerInstancesStateRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container_instances: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of up to 10 container instance IDs or full ARN entries.</p>"""
    status: "aws_sdk_ecs.types.container_instance_status.ContainerInstanceStatus"
    """<p>The container instance state to update the container instance with. The only valid values for this action are <code>ACTIVE</code> and <code>DRAINING</code>. A container instance can only be updated to <code>DRAINING</code> status once it has reached an <code>ACTIVE</code> state. If a container instance is in <code>REGISTERING</code>, <code>DEREGISTERING</code>, or <code>REGISTRATION_FAILED</code> state you can describe the container instance but can't update the container instance state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerInstancesStateRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import aws_sdk_ecs.types.string_list

    out["containerInstances"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
        value["container_instances"]
    )
    import aws_sdk_ecs.types.container_instance_status

    out["status"] = aws_sdk_ecs.types.container_instance_status.serialize_aws_json_1_1(
        value["status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerInstancesStateRequest:
    out: UpdateContainerInstancesStateRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "containerInstances" in data:
        import aws_sdk_ecs.types.string_list

        out["container_instances"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["containerInstances"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateContainerInstancesStateRequest.container_instances required"
        )
    if "status" in data:
        import aws_sdk_ecs.types.container_instance_status

        out["status"] = (
            aws_sdk_ecs.types.container_instance_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateContainerInstancesStateRequest.status required"
        )
    return out
