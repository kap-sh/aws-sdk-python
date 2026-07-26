"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentRevisionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.daemon_deployment_capacity_provider_list
    import capo_ecs.types.string


class DaemonDeploymentRevisionDetail(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon revision.</p>"""
    capacity_providers: NotRequired[
        "capo_ecs.types.daemon_deployment_capacity_provider_list.DaemonDeploymentCapacityProviderList"
    ]
    """<p>The capacity providers associated with this daemon revision during the deployment.</p>"""
    total_running_instance_count: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The total number of instances running daemon tasks for this revision.</p>"""
    total_draining_instance_count: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The total number of instances being drained for this revision during the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentRevisionDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "capacity_providers" in value:
        import capo_ecs.types.daemon_deployment_capacity_provider_list

        out["capacityProviders"] = (
            capo_ecs.types.daemon_deployment_capacity_provider_list.serialize_aws_json_1_1(
                value["capacity_providers"]
            )
        )
    if "total_running_instance_count" in value:
        out["totalRunningInstanceCount"] = value["total_running_instance_count"]
    if "total_draining_instance_count" in value:
        out["totalDrainingInstanceCount"] = value["total_draining_instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDeploymentRevisionDetail:
    out: DaemonDeploymentRevisionDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "capacityProviders" in data:
        import capo_ecs.types.daemon_deployment_capacity_provider_list

        out["capacity_providers"] = (
            capo_ecs.types.daemon_deployment_capacity_provider_list.deserialize_aws_json_1_1(
                data["capacityProviders"]
            )
        )
    if "totalRunningInstanceCount" in data:
        out["total_running_instance_count"] = data["totalRunningInstanceCount"]
    if "totalDrainingInstanceCount" in data:
        out["total_draining_instance_count"] = data["totalDrainingInstanceCount"]
    return out
