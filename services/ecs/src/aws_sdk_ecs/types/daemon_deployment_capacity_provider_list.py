"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentCapacityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_capacity_provider

DaemonDeploymentCapacityProviderList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment_capacity_provider.DaemonDeploymentCapacityProvider"
]
