"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteSpec``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_priority
    import aws_sdk_app_mesh.types.grpc_gateway_route
    import aws_sdk_app_mesh.types.http_gateway_route


class GatewayRouteSpec(TypedDict):
    priority: NotRequired[
        "aws_sdk_app_mesh.types.gateway_route_priority.GatewayRoutePriority"
    ]
    """<p>The ordering of the gateway routes spec.</p>"""
    http_route: NotRequired[
        "aws_sdk_app_mesh.types.http_gateway_route.HttpGatewayRoute"
    ]
    """<p>An object that represents the specification of an HTTP gateway route.</p>"""
    http2_route: NotRequired[
        "aws_sdk_app_mesh.types.http_gateway_route.HttpGatewayRoute"
    ]
    """<p>An object that represents the specification of an HTTP/2 gateway route.</p>"""
    grpc_route: NotRequired[
        "aws_sdk_app_mesh.types.grpc_gateway_route.GrpcGatewayRoute"
    ]
    """<p>An object that represents the specification of a gRPC gateway route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteSpec) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "http_route" in value:
        import aws_sdk_app_mesh.types.http_gateway_route

        out["httpRoute"] = aws_sdk_app_mesh.types.http_gateway_route.serialize_json(
            value["http_route"]
        )
    if "http2_route" in value:
        import aws_sdk_app_mesh.types.http_gateway_route

        out["http2Route"] = aws_sdk_app_mesh.types.http_gateway_route.serialize_json(
            value["http2_route"]
        )
    if "grpc_route" in value:
        import aws_sdk_app_mesh.types.grpc_gateway_route

        out["grpcRoute"] = aws_sdk_app_mesh.types.grpc_gateway_route.serialize_json(
            value["grpc_route"]
        )
    return out


def deserialize_json(data: dict) -> GatewayRouteSpec:
    out: GatewayRouteSpec = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "httpRoute" in data:
        import aws_sdk_app_mesh.types.http_gateway_route

        out["http_route"] = aws_sdk_app_mesh.types.http_gateway_route.deserialize_json(
            data["httpRoute"]
        )
    if "http2Route" in data:
        import aws_sdk_app_mesh.types.http_gateway_route

        out["http2_route"] = aws_sdk_app_mesh.types.http_gateway_route.deserialize_json(
            data["http2Route"]
        )
    if "grpcRoute" in data:
        import aws_sdk_app_mesh.types.grpc_gateway_route

        out["grpc_route"] = aws_sdk_app_mesh.types.grpc_gateway_route.deserialize_json(
            data["grpcRoute"]
        )
    return out
