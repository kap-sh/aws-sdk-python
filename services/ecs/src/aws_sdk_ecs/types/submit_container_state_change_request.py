"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitContainerStateChangeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.network_bindings
    import aws_sdk_ecs.types.string


class SubmitContainerStateChangeRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full ARN of the cluster that hosts the container.</p>"""
    task: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.</p>"""
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    runtime_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the state change request.</p>"""
    exit_code: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code that's returned for the state change request.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the state change request.</p>"""
    network_bindings: NotRequired["aws_sdk_ecs.types.network_bindings.NetworkBindings"]
    """<p>The network bindings of the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubmitContainerStateChangeRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "task" in value:
        out["task"] = value["task"]
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "runtime_id" in value:
        out["runtimeId"] = value["runtime_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "network_bindings" in value:
        import aws_sdk_ecs.types.network_bindings

        out["networkBindings"] = (
            aws_sdk_ecs.types.network_bindings.serialize_aws_json_1_1(
                value["network_bindings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitContainerStateChangeRequest:
    out: SubmitContainerStateChangeRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "task" in data:
        out["task"] = data["task"]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "runtimeId" in data:
        out["runtime_id"] = data["runtimeId"]
    if "status" in data:
        out["status"] = data["status"]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "networkBindings" in data:
        import aws_sdk_ecs.types.network_bindings

        out["network_bindings"] = (
            aws_sdk_ecs.types.network_bindings.deserialize_aws_json_1_1(
                data["networkBindings"]
            )
        )
    return out
