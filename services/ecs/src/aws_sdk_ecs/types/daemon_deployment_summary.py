"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonDeploymentSummary(TypedDict):
    daemon_deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon deployment.</p>"""
    daemon_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that hosts the daemon.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_status.DaemonDeploymentStatus"
    ]
    """<p>The status of the daemon deployment.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the daemon deployment is in the current status.</p>"""
    target_daemon_revision_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the daemon revision being deployed.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment was created.</p>"""
    started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment started.</p>"""
    stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment stopped.</p>"""
    finished_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment finished.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentSummary) -> dict:
    out: dict = {}
    if "daemon_deployment_arn" in value:
        out["daemonDeploymentArn"] = value["daemon_deployment_arn"]
    if "daemon_arn" in value:
        out["daemonArn"] = value["daemon_arn"]
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
    if "target_daemon_revision_arn" in value:
        out["targetDaemonRevisionArn"] = value["target_daemon_revision_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> DaemonDeploymentSummary:
    out: DaemonDeploymentSummary = {}  # type: ignore[typeddict-item]
    if "daemonDeploymentArn" in data:
        out["daemon_deployment_arn"] = data["daemonDeploymentArn"]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
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
    if "targetDaemonRevisionArn" in data:
        out["target_daemon_revision_arn"] = data["targetDaemonRevisionArn"]
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
