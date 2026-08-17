"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_revision_detail_list
    import capo_ecs.types.daemon_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class DaemonDetail(TypedDict, closed=True):
    daemon_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that the daemon is running in.</p>"""
    status: NotRequired["capo_ecs.types.daemon_status.DaemonStatus"]
    """<p>The status of the daemon.</p>"""
    current_revisions: NotRequired[
        "capo_ecs.types.daemon_revision_detail_list.DaemonRevisionDetailList"
    ]
    """<p>The current daemon revision details, including the running task counts per capacity provider.</p>"""
    deployment_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the most recent daemon deployment.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was created.</p>"""
    updated_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDetail) -> dict:
    out: dict = {}
    if "daemon_arn" in value:
        out["daemonArn"] = value["daemon_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "status" in value:
        import capo_ecs.types.daemon_status

        out["status"] = capo_ecs.types.daemon_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "current_revisions" in value:
        import capo_ecs.types.daemon_revision_detail_list

        out["currentRevisions"] = (
            capo_ecs.types.daemon_revision_detail_list.serialize_aws_json_1_1(
                value["current_revisions"]
            )
        )
    if "deployment_arn" in value:
        out["deploymentArn"] = value["deployment_arn"]
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_ecs.types.timestamp

        out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDetail:
    out: DaemonDetail = {}  # type: ignore[typeddict-item]
    if data.get("daemonArn") is not None:
        out["daemon_arn"] = data["daemonArn"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("status") is not None:
        import capo_ecs.types.daemon_status

        out["status"] = capo_ecs.types.daemon_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("currentRevisions") is not None:
        import capo_ecs.types.daemon_revision_detail_list

        out["current_revisions"] = (
            capo_ecs.types.daemon_revision_detail_list.deserialize_aws_json_1_1(
                data["currentRevisions"]
            )
        )
    if data.get("deploymentArn") is not None:
        out["deployment_arn"] = data["deploymentArn"]
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    return out
