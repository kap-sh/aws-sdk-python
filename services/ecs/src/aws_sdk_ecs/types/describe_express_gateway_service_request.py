"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_include_list
    import aws_sdk_ecs.types.string


class DescribeExpressGatewayServiceRequest(TypedDict):
    service_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to describe. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>"""
    include: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_include_list.ExpressGatewayServiceIncludeList"
    ]
    """<p>Specifies additional information to include in the response. Valid values are <code>TAGS</code> to include resource tags associated with the Express service.</p>"""
