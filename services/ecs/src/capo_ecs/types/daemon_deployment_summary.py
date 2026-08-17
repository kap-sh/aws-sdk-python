"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_deployment_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class DaemonDeploymentSummary(TypedDict, closed=True):
    daemon_deployment_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon deployment.</p>"""
    daemon_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that hosts the daemon.</p>"""
    status: NotRequired[
        "capo_ecs.types.daemon_deployment_status.DaemonDeploymentStatus"
    ]
    """<p>The status of the daemon deployment.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the daemon deployment is in the current status.</p>"""
    target_daemon_revision_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the daemon revision being deployed.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment was created.</p>"""
    started_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment started.</p>"""
    stopped_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time the daemon deployment stopped.</p>"""
    finished_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
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
        import capo_ecs.types.daemon_deployment_status

        out["status"] = capo_ecs.types.daemon_deployment_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "target_daemon_revision_arn" in value:
        out["targetDaemonRevisionArn"] = value["target_daemon_revision_arn"]
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "started_at" in value:
        import capo_ecs.types.timestamp

        out["startedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "stopped_at" in value:
        import capo_ecs.types.timestamp

        out["stoppedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["stopped_at"]
        )
    if "finished_at" in value:
        import capo_ecs.types.timestamp

        out["finishedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["finished_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDeploymentSummary:
    out: DaemonDeploymentSummary = {}  # type: ignore[typeddict-item]
    if data.get("daemonDeploymentArn") is not None:
        out["daemon_deployment_arn"] = data["daemonDeploymentArn"]
    if data.get("daemonArn") is not None:
        out["daemon_arn"] = data["daemonArn"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("status") is not None:
        import capo_ecs.types.daemon_deployment_status

        out["status"] = (
            capo_ecs.types.daemon_deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("targetDaemonRevisionArn") is not None:
        out["target_daemon_revision_arn"] = data["targetDaemonRevisionArn"]
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("startedAt") is not None:
        import capo_ecs.types.timestamp

        out["started_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if data.get("stoppedAt") is not None:
        import capo_ecs.types.timestamp

        out["stopped_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["stoppedAt"]
        )
    if data.get("finishedAt") is not None:
        import capo_ecs.types.timestamp

        out["finished_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["finishedAt"]
        )
    return out
