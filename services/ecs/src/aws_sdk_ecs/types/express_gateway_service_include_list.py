"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceIncludeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_include

ExpressGatewayServiceIncludeList: TypeAlias = list[
    "aws_sdk_ecs.types.express_gateway_service_include.ExpressGatewayServiceInclude"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceIncludeList) -> list:
    import aws_sdk_ecs.types.express_gateway_service_include

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.express_gateway_service_include.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExpressGatewayServiceIncludeList:
    import aws_sdk_ecs.types.express_gateway_service_include

    out: ExpressGatewayServiceIncludeList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.express_gateway_service_include.deserialize_aws_json_1_1(
                item
            )
        )
    return out
