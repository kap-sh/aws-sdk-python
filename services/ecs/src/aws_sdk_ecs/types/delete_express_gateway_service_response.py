"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteExpressGatewayServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ecs_express_gateway_service


class DeleteExpressGatewayServiceResponse(TypedDict):
    service: NotRequired[
        "aws_sdk_ecs.types.ecs_express_gateway_service.ECSExpressGatewayService"
    ]
    """<p>The full description of the deleted express service.</p>"""
