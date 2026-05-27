"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeployment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_circuit_breaker
    import aws_sdk_ecs.types.daemon_deployment_alarms
    import aws_sdk_ecs.types.daemon_deployment_configuration
    import aws_sdk_ecs.types.daemon_deployment_revision_detail
    import aws_sdk_ecs.types.daemon_deployment_revision_detail_list
    import aws_sdk_ecs.types.daemon_deployment_status
    import aws_sdk_ecs.types.daemon_rollback
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonDeployment(TypedDict):
    daemon_deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon deployment.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that hosts the daemon.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_status.DaemonDeploymentStatus"
    ]
    """<p>The status of the daemon deployment.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the daemon deployment is in the current status.</p>"""
    target_daemon_revision: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_revision_detail.DaemonDeploymentRevisionDetail"
    ]
    """<p>The daemon revision being deployed.</p>"""
    source_daemon_revisions: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_revision_detail_list.DaemonDeploymentRevisionDetailList"
    ]
    """<p>The currently deployed daemon revisions that are being replaced.</p>"""
    circuit_breaker: NotRequired[
        "aws_sdk_ecs.types.daemon_circuit_breaker.DaemonCircuitBreaker"
    ]
    """<p>The circuit breaker configuration that determines when a daemon deployment has failed.</p>"""
    alarms: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_alarms.DaemonDeploymentAlarms"
    ]
    """<p>The CloudWatch alarms that determine when a daemon deployment fails.</p>"""
    rollback: NotRequired["aws_sdk_ecs.types.daemon_rollback.DaemonRollback"]
    """<p>The rollback options for the daemon deployment.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
    ]
    """<p>The deployment configuration used for this daemon deployment.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment stopped. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    finished_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment finished. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
