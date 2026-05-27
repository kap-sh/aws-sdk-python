"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment

DaemonDeploymentList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment.DaemonDeployment"
]
