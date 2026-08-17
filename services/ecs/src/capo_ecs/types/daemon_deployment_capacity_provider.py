"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentCapacityProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string


class DaemonDeploymentCapacityProvider(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    running_instance_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instances running daemon tasks on this capacity provider.</p>"""
    draining_instance_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instances being drained on this capacity provider during the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentCapacityProvider) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "running_instance_count" in value:
        out["runningInstanceCount"] = value["running_instance_count"]
    if "draining_instance_count" in value:
        out["drainingInstanceCount"] = value["draining_instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDeploymentCapacityProvider:
    out: DaemonDeploymentCapacityProvider = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("runningInstanceCount") is not None:
        out["running_instance_count"] = data["runningInstanceCount"]
    if data.get("drainingInstanceCount") is not None:
        out["draining_instance_count"] = data["drainingInstanceCount"]
    return out
