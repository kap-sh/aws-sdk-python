"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceIncludeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_service_include

ExpressGatewayServiceIncludeList: TypeAlias = list[
    "capo_ecs.types.express_gateway_service_include.ExpressGatewayServiceInclude"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceIncludeList) -> list:
    import capo_ecs.types.express_gateway_service_include

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.express_gateway_service_include.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExpressGatewayServiceIncludeList:
    import capo_ecs.types.express_gateway_service_include

    out: ExpressGatewayServiceIncludeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.express_gateway_service_include.deserialize_aws_json_1_1(
                item
            )
        )
    return out
