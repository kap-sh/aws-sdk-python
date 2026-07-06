"""Generated from Smithy shape ``com.amazonaws.ecs#UpdatedExpressGatewayService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_configuration
    import aws_sdk_ecs.types.express_gateway_service_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class UpdatedExpressGatewayService(TypedDict, closed=True):
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the Express service that is being updated.</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The cluster associated with the Express service that is being updated.</p>"""
    service_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the Express service that is being updated.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_status.ExpressGatewayServiceStatus"
    ]
    """<p>The status of the Express service that is being updated.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_configuration.ExpressGatewayServiceConfiguration"
    ]
    """<p>The configuration to which the current Express service is being updated to.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service that is being updated was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service that is being updated was most recently updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatedExpressGatewayService) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "status" in value:
        import aws_sdk_ecs.types.express_gateway_service_status

        out["status"] = (
            aws_sdk_ecs.types.express_gateway_service_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "target_configuration" in value:
        import aws_sdk_ecs.types.express_gateway_service_configuration

        out["targetConfiguration"] = (
            aws_sdk_ecs.types.express_gateway_service_configuration.serialize_aws_json_1_1(
                value["target_configuration"]
            )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatedExpressGatewayService:
    out: UpdatedExpressGatewayService = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "status" in data:
        import aws_sdk_ecs.types.express_gateway_service_status

        out["status"] = (
            aws_sdk_ecs.types.express_gateway_service_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "targetConfiguration" in data:
        import aws_sdk_ecs.types.express_gateway_service_configuration

        out["target_configuration"] = (
            aws_sdk_ecs.types.express_gateway_service_configuration.deserialize_aws_json_1_1(
                data["targetConfiguration"]
            )
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
    return out
