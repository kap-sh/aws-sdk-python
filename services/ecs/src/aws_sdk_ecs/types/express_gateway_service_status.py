"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_status_code
    import aws_sdk_ecs.types.string


class ExpressGatewayServiceStatus(TypedDict):
    status_code: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_status_code.ExpressGatewayServiceStatusCode"
    ]
    """<p>The status of the Express service.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the Express service is in the current status.</p>"""
