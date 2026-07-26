"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.gateway_route_ref

GatewayRouteList: TypeAlias = list[
    "capo_app_mesh.types.gateway_route_ref.GatewayRouteRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteList) -> list:
    import capo_app_mesh.types.gateway_route_ref

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.gateway_route_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> GatewayRouteList:
    import capo_app_mesh.types.gateway_route_ref

    out: GatewayRouteList = []
    for item in data:
        out.append(capo_app_mesh.types.gateway_route_ref.deserialize_json(item))
    return out
