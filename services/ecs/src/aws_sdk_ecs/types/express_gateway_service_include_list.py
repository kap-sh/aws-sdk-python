"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceIncludeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_include

ExpressGatewayServiceIncludeList: TypeAlias = list[
    "aws_sdk_ecs.types.express_gateway_service_include.ExpressGatewayServiceInclude"
]
