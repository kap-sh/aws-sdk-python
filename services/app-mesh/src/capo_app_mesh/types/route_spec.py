"""Generated from Smithy shape ``com.amazonaws.appmesh#RouteSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_route
    import capo_app_mesh.types.http_route
    import capo_app_mesh.types.route_priority
    import capo_app_mesh.types.tcp_route


class RouteSpec(TypedDict, closed=True):
    priority: NotRequired["capo_app_mesh.types.route_priority.RoutePriority"]
    """<p>The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.</p>"""
    http_route: NotRequired["capo_app_mesh.types.http_route.HttpRoute"]
    """<p>An object that represents the specification of an HTTP route.</p>"""
    tcp_route: NotRequired["capo_app_mesh.types.tcp_route.TcpRoute"]
    """<p>An object that represents the specification of a TCP route.</p>"""
    http2_route: NotRequired["capo_app_mesh.types.http_route.HttpRoute"]
    """<p>An object that represents the specification of an HTTP/2 route.</p>"""
    grpc_route: NotRequired["capo_app_mesh.types.grpc_route.GrpcRoute"]
    """<p>An object that represents the specification of a gRPC route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpec) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "http_route" in value:
        import capo_app_mesh.types.http_route

        out["httpRoute"] = capo_app_mesh.types.http_route.serialize_json(
            value["http_route"]
        )
    if "tcp_route" in value:
        import capo_app_mesh.types.tcp_route

        out["tcpRoute"] = capo_app_mesh.types.tcp_route.serialize_json(
            value["tcp_route"]
        )
    if "http2_route" in value:
        import capo_app_mesh.types.http_route

        out["http2Route"] = capo_app_mesh.types.http_route.serialize_json(
            value["http2_route"]
        )
    if "grpc_route" in value:
        import capo_app_mesh.types.grpc_route

        out["grpcRoute"] = capo_app_mesh.types.grpc_route.serialize_json(
            value["grpc_route"]
        )
    return out


def deserialize_json(data: dict) -> RouteSpec:
    out: RouteSpec = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "httpRoute" in data:
        import capo_app_mesh.types.http_route

        out["http_route"] = capo_app_mesh.types.http_route.deserialize_json(
            data["httpRoute"]
        )
    if "tcpRoute" in data:
        import capo_app_mesh.types.tcp_route

        out["tcp_route"] = capo_app_mesh.types.tcp_route.deserialize_json(
            data["tcpRoute"]
        )
    if "http2Route" in data:
        import capo_app_mesh.types.http_route

        out["http2_route"] = capo_app_mesh.types.http_route.deserialize_json(
            data["http2Route"]
        )
    if "grpcRoute" in data:
        import capo_app_mesh.types.grpc_route

        out["grpc_route"] = capo_app_mesh.types.grpc_route.deserialize_json(
            data["grpcRoute"]
        )
    return out
