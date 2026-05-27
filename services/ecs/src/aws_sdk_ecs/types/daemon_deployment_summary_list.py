"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_summary

DaemonDeploymentSummaryList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment_summary.DaemonDeploymentSummary"
]
