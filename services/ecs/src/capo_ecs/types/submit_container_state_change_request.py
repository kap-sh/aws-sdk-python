"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitContainerStateChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.network_bindings
    import capo_ecs.types.string


class SubmitContainerStateChangeRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full ARN of the cluster that hosts the container.</p>"""
    task: NotRequired["capo_ecs.types.string.String"]
    """<p>The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.</p>"""
    container_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    runtime_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    status: NotRequired["capo_ecs.types.string.String"]
    """<p>The status of the state change request.</p>"""
    exit_code: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code that's returned for the state change request.</p>"""
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason for the state change request.</p>"""
    network_bindings: NotRequired["capo_ecs.types.network_bindings.NetworkBindings"]
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
        import capo_ecs.types.network_bindings

        out["networkBindings"] = capo_ecs.types.network_bindings.serialize_aws_json_1_1(
            value["network_bindings"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitContainerStateChangeRequest:
    out: SubmitContainerStateChangeRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("task") is not None:
        out["task"] = data["task"]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    if data.get("runtimeId") is not None:
        out["runtime_id"] = data["runtimeId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("exitCode") is not None:
        out["exit_code"] = data["exitCode"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("networkBindings") is not None:
        import capo_ecs.types.network_bindings

        out["network_bindings"] = (
            capo_ecs.types.network_bindings.deserialize_aws_json_1_1(
                data["networkBindings"]
            )
        )
    return out
