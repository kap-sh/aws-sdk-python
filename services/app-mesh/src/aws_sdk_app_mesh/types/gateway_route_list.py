"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_ref

GatewayRouteList: TypeAlias = list[
    "aws_sdk_app_mesh.types.gateway_route_ref.GatewayRouteRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteList) -> list:
    import aws_sdk_app_mesh.types.gateway_route_ref

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.gateway_route_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> GatewayRouteList:
    import aws_sdk_app_mesh.types.gateway_route_ref

    out: GatewayRouteList = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.gateway_route_ref.deserialize_json(item))
    return out
