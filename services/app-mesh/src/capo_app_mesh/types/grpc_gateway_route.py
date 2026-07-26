"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcGatewayRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_gateway_route_action
    import capo_app_mesh.types.grpc_gateway_route_match


class GrpcGatewayRoute(TypedDict, closed=True):
    match: "capo_app_mesh.types.grpc_gateway_route_match.GrpcGatewayRouteMatch"
    """<p>An object that represents the criteria for determining a request match.</p>"""
    action: "capo_app_mesh.types.grpc_gateway_route_action.GrpcGatewayRouteAction"
    """<p>An object that represents the action to take if a match is determined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcGatewayRoute) -> dict:
    out: dict = {}
    import capo_app_mesh.types.grpc_gateway_route_match

    out["match"] = capo_app_mesh.types.grpc_gateway_route_match.serialize_json(
        value["match"]
    )
    import capo_app_mesh.types.grpc_gateway_route_action

    out["action"] = capo_app_mesh.types.grpc_gateway_route_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> GrpcGatewayRoute:
    out: GrpcGatewayRoute = {}  # type: ignore[typeddict-item]
    if "match" in data:
        import capo_app_mesh.types.grpc_gateway_route_match

        out["match"] = capo_app_mesh.types.grpc_gateway_route_match.deserialize_json(
            data["match"]
        )
    else:
        raise DeserializationError("GrpcGatewayRoute.match required")
    if "action" in data:
        import capo_app_mesh.types.grpc_gateway_route_action

        out["action"] = capo_app_mesh.types.grpc_gateway_route_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("GrpcGatewayRoute.action required")
    return out
