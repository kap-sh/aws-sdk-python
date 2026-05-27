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
