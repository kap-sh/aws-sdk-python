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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeployment) -> dict:
    out: dict = {}
    if "daemon_deployment_arn" in value:
        out["daemonDeploymentArn"] = value["daemon_deployment_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "status" in value:
        import aws_sdk_ecs.types.daemon_deployment_status

        out["status"] = (
            aws_sdk_ecs.types.daemon_deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "target_daemon_revision" in value:
        import aws_sdk_ecs.types.daemon_deployment_revision_detail

        out["targetDaemonRevision"] = (
            aws_sdk_ecs.types.daemon_deployment_revision_detail.serialize_aws_json_1_1(
                value["target_daemon_revision"]
            )
        )
    if "source_daemon_revisions" in value:
        import aws_sdk_ecs.types.daemon_deployment_revision_detail_list

        out["sourceDaemonRevisions"] = (
            aws_sdk_ecs.types.daemon_deployment_revision_detail_list.serialize_aws_json_1_1(
                value["source_daemon_revisions"]
            )
        )
    if "circuit_breaker" in value:
        import aws_sdk_ecs.types.daemon_circuit_breaker

        out["circuitBreaker"] = (
            aws_sdk_ecs.types.daemon_circuit_breaker.serialize_aws_json_1_1(
                value["circuit_breaker"]
            )
        )
    if "alarms" in value:
        import aws_sdk_ecs.types.daemon_deployment_alarms

        out["alarms"] = (
            aws_sdk_ecs.types.daemon_deployment_alarms.serialize_aws_json_1_1(
                value["alarms"]
            )
        )
    if "rollback" in value:
        import aws_sdk_ecs.types.daemon_rollback

        out["rollback"] = aws_sdk_ecs.types.daemon_rollback.serialize_aws_json_1_1(
            value["rollback"]
        )
    if "deployment_configuration" in value:
        import aws_sdk_ecs.types.daemon_deployment_configuration

        out["deploymentConfiguration"] = (
            aws_sdk_ecs.types.daemon_deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "started_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["startedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "stopped_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["stoppedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["stopped_at"]
        )
    if "finished_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["finishedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["finished_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDeployment:
    out: DaemonDeployment = {}  # type: ignore[typeddict-item]
    if "daemonDeploymentArn" in data:
        out["daemon_deployment_arn"] = data["daemonDeploymentArn"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "status" in data:
        import aws_sdk_ecs.types.daemon_deployment_status

        out["status"] = (
            aws_sdk_ecs.types.daemon_deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "targetDaemonRevision" in data:
        import aws_sdk_ecs.types.daemon_deployment_revision_detail

        out["target_daemon_revision"] = (
            aws_sdk_ecs.types.daemon_deployment_revision_detail.deserialize_aws_json_1_1(
                data["targetDaemonRevision"]
            )
        )
    if "sourceDaemonRevisions" in data:
        import aws_sdk_ecs.types.daemon_deployment_revision_detail_list

        out["source_daemon_revisions"] = (
            aws_sdk_ecs.types.daemon_deployment_revision_detail_list.deserialize_aws_json_1_1(
                data["sourceDaemonRevisions"]
            )
        )
    if "circuitBreaker" in data:
        import aws_sdk_ecs.types.daemon_circuit_breaker

        out["circuit_breaker"] = (
            aws_sdk_ecs.types.daemon_circuit_breaker.deserialize_aws_json_1_1(
                data["circuitBreaker"]
            )
        )
    if "alarms" in data:
        import aws_sdk_ecs.types.daemon_deployment_alarms

        out["alarms"] = (
            aws_sdk_ecs.types.daemon_deployment_alarms.deserialize_aws_json_1_1(
                data["alarms"]
            )
        )
    if "rollback" in data:
        import aws_sdk_ecs.types.daemon_rollback

        out["rollback"] = aws_sdk_ecs.types.daemon_rollback.deserialize_aws_json_1_1(
            data["rollback"]
        )
    if "deploymentConfiguration" in data:
        import aws_sdk_ecs.types.daemon_deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_ecs.types.daemon_deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "startedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["started_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if "stoppedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["stopped_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["stoppedAt"]
        )
    if "finishedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["finished_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["finishedAt"]
        )
    return out
