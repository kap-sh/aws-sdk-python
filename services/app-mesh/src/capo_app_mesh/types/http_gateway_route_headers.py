"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpGatewayRouteHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.http_gateway_route_header

HttpGatewayRouteHeaders: TypeAlias = list[
    "capo_app_mesh.types.http_gateway_route_header.HttpGatewayRouteHeader"
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpGatewayRouteHeaders) -> list:
    import capo_app_mesh.types.http_gateway_route_header

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.http_gateway_route_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> HttpGatewayRouteHeaders:
    import capo_app_mesh.types.http_gateway_route_header

    out: HttpGatewayRouteHeaders = []
    for item in data:
        out.append(capo_app_mesh.types.http_gateway_route_header.deserialize_json(item))
    return out
