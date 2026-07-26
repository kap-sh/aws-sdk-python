"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_deployment

DaemonDeploymentList: TypeAlias = list[
    "capo_ecs.types.daemon_deployment.DaemonDeployment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentList) -> list:
    import capo_ecs.types.daemon_deployment

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_deployment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonDeploymentList:
    import capo_ecs.types.daemon_deployment

    out: DaemonDeploymentList = []
    for item in data:
        out.append(capo_ecs.types.daemon_deployment.deserialize_aws_json_1_1(item))
    return out
