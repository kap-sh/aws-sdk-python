"""Generated from Smithy shape ``com.amazonaws.ecs#UpdatedExpressGatewayService``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_configuration
    import aws_sdk_ecs.types.express_gateway_service_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class UpdatedExpressGatewayService(TypedDict):
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
