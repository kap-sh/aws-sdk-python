"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.gateway_route_priority
    import capo_app_mesh.types.grpc_gateway_route
    import capo_app_mesh.types.http_gateway_route


class GatewayRouteSpec(TypedDict, closed=True):
    priority: NotRequired[
        "capo_app_mesh.types.gateway_route_priority.GatewayRoutePriority"
    ]
    """<p>The ordering of the gateway routes spec.</p>"""
    http_route: NotRequired["capo_app_mesh.types.http_gateway_route.HttpGatewayRoute"]
    """<p>An object that represents the specification of an HTTP gateway route.</p>"""
    http2_route: NotRequired["capo_app_mesh.types.http_gateway_route.HttpGatewayRoute"]
    """<p>An object that represents the specification of an HTTP/2 gateway route.</p>"""
    grpc_route: NotRequired["capo_app_mesh.types.grpc_gateway_route.GrpcGatewayRoute"]
    """<p>An object that represents the specification of a gRPC gateway route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteSpec) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "http_route" in value:
        import capo_app_mesh.types.http_gateway_route

        out["httpRoute"] = capo_app_mesh.types.http_gateway_route.serialize_json(
            value["http_route"]
        )
    if "http2_route" in value:
        import capo_app_mesh.types.http_gateway_route

        out["http2Route"] = capo_app_mesh.types.http_gateway_route.serialize_json(
            value["http2_route"]
        )
    if "grpc_route" in value:
        import capo_app_mesh.types.grpc_gateway_route

        out["grpcRoute"] = capo_app_mesh.types.grpc_gateway_route.serialize_json(
            value["grpc_route"]
        )
    return out


def deserialize_json(data: dict) -> GatewayRouteSpec:
    out: GatewayRouteSpec = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "httpRoute" in data:
        import capo_app_mesh.types.http_gateway_route

        out["http_route"] = capo_app_mesh.types.http_gateway_route.deserialize_json(
            data["httpRoute"]
        )
    if "http2Route" in data:
        import capo_app_mesh.types.http_gateway_route

        out["http2_route"] = capo_app_mesh.types.http_gateway_route.deserialize_json(
            data["http2Route"]
        )
    if "grpcRoute" in data:
        import capo_app_mesh.types.grpc_gateway_route

        out["grpc_route"] = capo_app_mesh.types.grpc_gateway_route.deserialize_json(
            data["grpcRoute"]
        )
    return out
