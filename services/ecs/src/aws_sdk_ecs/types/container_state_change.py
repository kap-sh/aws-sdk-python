"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerStateChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.network_bindings
    import aws_sdk_ecs.types.string


class ContainerStateChange(TypedDict, closed=True):
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    image_digest: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container image SHA 256 digest.</p>"""
    runtime_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    exit_code: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code for the container, if the state change is a result of the container exiting.</p>"""
    network_bindings: NotRequired["aws_sdk_ecs.types.network_bindings.NetworkBindings"]
    """<p>Any network bindings that are associated with the container.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the state change.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerStateChange) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "runtime_id" in value:
        out["runtimeId"] = value["runtime_id"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "network_bindings" in value:
        import aws_sdk_ecs.types.network_bindings

        out["networkBindings"] = (
            aws_sdk_ecs.types.network_bindings.serialize_aws_json_1_1(
                value["network_bindings"]
            )
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerStateChange:
    out: ContainerStateChange = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "runtimeId" in data:
        out["runtime_id"] = data["runtimeId"]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "networkBindings" in data:
        import aws_sdk_ecs.types.network_bindings

        out["network_bindings"] = (
            aws_sdk_ecs.types.network_bindings.deserialize_aws_json_1_1(
                data["networkBindings"]
            )
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    if "status" in data:
        out["status"] = data["status"]
    return out
