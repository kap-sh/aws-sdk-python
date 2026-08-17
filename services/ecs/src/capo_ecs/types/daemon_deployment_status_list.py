"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_deployment_status

DaemonDeploymentStatusList: TypeAlias = list[
    "capo_ecs.types.daemon_deployment_status.DaemonDeploymentStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentStatusList) -> list:
    import capo_ecs.types.daemon_deployment_status

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_deployment_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonDeploymentStatusList:
    import capo_ecs.types.daemon_deployment_status

    out: DaemonDeploymentStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.daemon_deployment_status.deserialize_aws_json_1_1(item)
        )
    return out
