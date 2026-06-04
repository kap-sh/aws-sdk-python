"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_configuration

ExpressGatewayServiceConfigurations: TypeAlias = list[
    "aws_sdk_ecs.types.express_gateway_service_configuration.ExpressGatewayServiceConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceConfigurations) -> list:
    import aws_sdk_ecs.types.express_gateway_service_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.express_gateway_service_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExpressGatewayServiceConfigurations:
    import aws_sdk_ecs.types.express_gateway_service_configuration

    out: ExpressGatewayServiceConfigurations = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.express_gateway_service_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
