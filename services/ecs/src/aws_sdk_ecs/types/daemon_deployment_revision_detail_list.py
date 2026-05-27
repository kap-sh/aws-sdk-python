"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentRevisionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_revision_detail

DaemonDeploymentRevisionDetailList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment_revision_detail.DaemonDeploymentRevisionDetail"
]
