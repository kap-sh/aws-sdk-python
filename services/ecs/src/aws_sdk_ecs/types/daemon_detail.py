"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_revision_detail_list
    import aws_sdk_ecs.types.daemon_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonDetail(TypedDict, closed=True):
    daemon_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that the daemon is running in.</p>"""
    status: NotRequired["aws_sdk_ecs.types.daemon_status.DaemonStatus"]
    """<p>The status of the daemon.</p>"""
    current_revisions: NotRequired[
        "aws_sdk_ecs.types.daemon_revision_detail_list.DaemonRevisionDetailList"
    ]
    """<p>The current daemon revision details, including the running task counts per capacity provider.</p>"""
    deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the most recent daemon deployment.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDetail) -> dict:
    out: dict = {}
    if "daemon_arn" in value:
        out["daemonArn"] = value["daemon_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "status" in value:
        import aws_sdk_ecs.types.daemon_status

        out["status"] = aws_sdk_ecs.types.daemon_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "current_revisions" in value:
        import aws_sdk_ecs.types.daemon_revision_detail_list

        out["currentRevisions"] = (
            aws_sdk_ecs.types.daemon_revision_detail_list.serialize_aws_json_1_1(
                value["current_revisions"]
            )
        )
    if "deployment_arn" in value:
        out["deploymentArn"] = value["deployment_arn"]
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["updatedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDetail:
    out: DaemonDetail = {}  # type: ignore[typeddict-item]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "status" in data:
        import aws_sdk_ecs.types.daemon_status

        out["status"] = aws_sdk_ecs.types.daemon_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "currentRevisions" in data:
        import aws_sdk_ecs.types.daemon_revision_detail_list

        out["current_revisions"] = (
            aws_sdk_ecs.types.daemon_revision_detail_list.deserialize_aws_json_1_1(
                data["currentRevisions"]
            )
        )
    if "deploymentArn" in data:
        out["deployment_arn"] = data["deploymentArn"]
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    return out
