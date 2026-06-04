"""Generated from Smithy shape ``com.amazonaws.ecs#ECSExpressGatewayService``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_configurations
    import aws_sdk_ecs.types.express_gateway_service_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.timestamp


class ECSExpressGatewayService(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full ARN of the cluster that hosts the Express service.</p>"""
    service_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the Express service.</p>"""
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN that identifies the Express service.</p>"""
    infrastructure_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the infrastructure role that manages Amazon Web Services resources for the Express service.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_status.ExpressGatewayServiceStatus"
    ]
    """<p>The current status of the Express service.</p>"""
    current_deployment: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The current deployment configuration for the Express service.</p>"""
    active_configurations: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_configurations.ExpressGatewayServiceConfigurations"
    ]
    """<p>The list of active service configurations for the Express service.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata applied to the Express service.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSExpressGatewayService) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "infrastructure_role_arn" in value:
        out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "status" in value:
        import aws_sdk_ecs.types.express_gateway_service_status

        out["status"] = (
            aws_sdk_ecs.types.express_gateway_service_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "current_deployment" in value:
        out["currentDeployment"] = value["current_deployment"]
    if "active_configurations" in value:
        import aws_sdk_ecs.types.express_gateway_service_configurations

        out["activeConfigurations"] = (
            aws_sdk_ecs.types.express_gateway_service_configurations.serialize_aws_json_1_1(
                value["active_configurations"]
            )
        )
    if "tags" in value:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
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


def deserialize_aws_json_1_1(data: dict) -> ECSExpressGatewayService:
    out: ECSExpressGatewayService = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "infrastructureRoleArn" in data:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    if "status" in data:
        import aws_sdk_ecs.types.express_gateway_service_status

        out["status"] = (
            aws_sdk_ecs.types.express_gateway_service_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "currentDeployment" in data:
        out["current_deployment"] = data["currentDeployment"]
    if "activeConfigurations" in data:
        import aws_sdk_ecs.types.express_gateway_service_configurations

        out["active_configurations"] = (
            aws_sdk_ecs.types.express_gateway_service_configurations.deserialize_aws_json_1_1(
                data["activeConfigurations"]
            )
        )
    if "tags" in data:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
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
