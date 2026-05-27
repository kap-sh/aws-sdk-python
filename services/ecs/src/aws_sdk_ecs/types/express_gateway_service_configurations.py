"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_configuration

ExpressGatewayServiceConfigurations: TypeAlias = list[
    "aws_sdk_ecs.types.express_gateway_service_configuration.ExpressGatewayServiceConfiguration"
]
