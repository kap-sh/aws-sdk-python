"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerStateChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.network_bindings
    import capo_ecs.types.string


class ContainerStateChange(TypedDict, closed=True):
    container_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    image_digest: NotRequired["capo_ecs.types.string.String"]
    """<p>The container image SHA 256 digest.</p>"""
    runtime_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    exit_code: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code for the container, if the state change is a result of the container exiting.</p>"""
    network_bindings: NotRequired["capo_ecs.types.network_bindings.NetworkBindings"]
    """<p>Any network bindings that are associated with the container.</p>"""
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason for the state change.</p>"""
    status: NotRequired["capo_ecs.types.string.String"]
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
        import capo_ecs.types.network_bindings

        out["networkBindings"] = capo_ecs.types.network_bindings.serialize_aws_json_1_1(
            value["network_bindings"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerStateChange:
    out: ContainerStateChange = {}  # type: ignore[typeddict-item]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    if data.get("imageDigest") is not None:
        out["image_digest"] = data["imageDigest"]
    if data.get("runtimeId") is not None:
        out["runtime_id"] = data["runtimeId"]
    if data.get("exitCode") is not None:
        out["exit_code"] = data["exitCode"]
    if data.get("networkBindings") is not None:
        import capo_ecs.types.network_bindings

        out["network_bindings"] = (
            capo_ecs.types.network_bindings.deserialize_aws_json_1_1(
                data["networkBindings"]
            )
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
