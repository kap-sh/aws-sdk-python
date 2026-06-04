"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentCapacityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_capacity_provider

DaemonDeploymentCapacityProviderList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment_capacity_provider.DaemonDeploymentCapacityProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentCapacityProviderList) -> list:
    import aws_sdk_ecs.types.daemon_deployment_capacity_provider

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.daemon_deployment_capacity_provider.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonDeploymentCapacityProviderList:
    import aws_sdk_ecs.types.daemon_deployment_capacity_provider

    out: DaemonDeploymentCapacityProviderList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.daemon_deployment_capacity_provider.deserialize_aws_json_1_1(
                item
            )
        )
    return out
