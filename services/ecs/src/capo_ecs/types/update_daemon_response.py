"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateDaemonResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class UpdateDaemonResponse(TypedDict, closed=True):
    daemon_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    status: NotRequired["capo_ecs.types.daemon_status.DaemonStatus"]
    """<p>The status of the daemon.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was created.</p>"""
    updated_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was last updated.</p>"""
    deployment_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon deployment that was triggered by the update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDaemonResponse) -> dict:
    out: dict = {}
    if "daemon_arn" in value:
        out["daemonArn"] = value["daemon_arn"]
    if "status" in value:
        import capo_ecs.types.daemon_status

        out["status"] = capo_ecs.types.daemon_status.serialize_aws_json_1_1(
            value["status"]
        )
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
    if "deployment_arn" in value:
        out["deploymentArn"] = value["deployment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDaemonResponse:
    out: UpdateDaemonResponse = {}  # type: ignore[typeddict-item]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
    if "status" in data:
        import capo_ecs.types.daemon_status

        out["status"] = capo_ecs.types.daemon_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "createdAt" in data:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    if "deploymentArn" in data:
        out["deployment_arn"] = data["deploymentArn"]
    return out
