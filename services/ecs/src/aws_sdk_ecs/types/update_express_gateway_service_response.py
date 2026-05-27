"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateExpressGatewayServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.updated_express_gateway_service


class UpdateExpressGatewayServiceResponse(TypedDict):
    service: NotRequired[
        "aws_sdk_ecs.types.updated_express_gateway_service.UpdatedExpressGatewayService"
    ]
    """<p>The full description of your express gateway service following the update call.</p>"""
