"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentBrief``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ServiceDeploymentBrief(TypedDict, closed=True):
    service_deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service deployment.</p>"""
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service for this service deployment.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the cluster that hosts the service.</p>"""
    started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    finished_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment completed. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    target_service_revision_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service revision being deplyed.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.service_deployment_status.ServiceDeploymentStatus"
    ]
    """<p>The status of the service deployment</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the service deployment is in the current status. For example, the circuit breaker detected a deployment failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeploymentBrief) -> dict:
    out: dict = {}
    if "service_deployment_arn" in value:
        out["serviceDeploymentArn"] = value["service_deployment_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "started_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["startedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "finished_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["finishedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["finished_at"]
        )
    if "target_service_revision_arn" in value:
        out["targetServiceRevisionArn"] = value["target_service_revision_arn"]
    if "status" in value:
        import aws_sdk_ecs.types.service_deployment_status

        out["status"] = (
            aws_sdk_ecs.types.service_deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceDeploymentBrief:
    out: ServiceDeploymentBrief = {}  # type: ignore[typeddict-item]
    if "serviceDeploymentArn" in data:
        out["service_deployment_arn"] = data["serviceDeploymentArn"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "startedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["started_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "finishedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["finished_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["finishedAt"]
        )
    if "targetServiceRevisionArn" in data:
        out["target_service_revision_arn"] = data["targetServiceRevisionArn"]
    if "status" in data:
        import aws_sdk_ecs.types.service_deployment_status

        out["status"] = (
            aws_sdk_ecs.types.service_deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
