"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_status

DaemonDeploymentStatusList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment_status.DaemonDeploymentStatus"
]
