"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DeleteDaemonResponse(TypedDict):
    daemon_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    status: NotRequired["aws_sdk_ecs.types.daemon_status.DaemonStatus"]
    """<p>The status of the daemon. After you call <code>DeleteDaemon</code>, the status changes to <code>DELETE_IN_PROGRESS</code>.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was last updated.</p>"""
    deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon deployment that was triggered by the delete operation. This deployment drains existing daemon tasks from the container instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDaemonResponse) -> dict:
    out: dict = {}
    if "daemon_arn" in value:
        out["daemonArn"] = value["daemon_arn"]
    if "status" in value:
        import aws_sdk_ecs.types.daemon_status

        out["status"] = aws_sdk_ecs.types.daemon_status.serialize_aws_json_1_1(
            value["status"]
        )
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
    if "deployment_arn" in value:
        out["deploymentArn"] = value["deployment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDaemonResponse:
    out: DeleteDaemonResponse = {}  # type: ignore[typeddict-item]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
    if "status" in data:
        import aws_sdk_ecs.types.daemon_status

        out["status"] = aws_sdk_ecs.types.daemon_status.deserialize_aws_json_1_1(
            data["status"]
        )
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
    if "deploymentArn" in data:
        out["deployment_arn"] = data["deploymentArn"]
    return out
