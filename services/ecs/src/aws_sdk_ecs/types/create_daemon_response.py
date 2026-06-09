"""Generated from Smithy shape ``com.amazonaws.ecs#CreateDaemonResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class CreateDaemonResponse(TypedDict):
    daemon_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    status: NotRequired["aws_sdk_ecs.types.daemon_status.DaemonStatus"]
    """<p>The status of the daemon.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was created.</p>"""
    deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the initial daemon deployment. This deployment places daemon tasks on each container instance of the specified capacity providers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDaemonResponse) -> dict:
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
    if "deployment_arn" in value:
        out["deploymentArn"] = value["deployment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDaemonResponse:
    out: CreateDaemonResponse = {}  # type: ignore[typeddict-item]
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
    if "deploymentArn" in data:
        out["deployment_arn"] = data["deploymentArn"]
    return out
