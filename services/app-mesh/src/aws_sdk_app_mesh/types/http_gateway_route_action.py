"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpGatewayRouteAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_target
    import aws_sdk_app_mesh.types.http_gateway_route_rewrite


class HttpGatewayRouteAction(TypedDict, closed=True):
    target: "aws_sdk_app_mesh.types.gateway_route_target.GatewayRouteTarget"
    """<p>An object that represents the target that traffic is routed to when a request matches the gateway route.</p>"""
    rewrite: NotRequired[
        "aws_sdk_app_mesh.types.http_gateway_route_rewrite.HttpGatewayRouteRewrite"
    ]
    """<p>The gateway route action to rewrite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpGatewayRouteAction) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.gateway_route_target

    out["target"] = aws_sdk_app_mesh.types.gateway_route_target.serialize_json(
        value["target"]
    )
    if "rewrite" in value:
        import aws_sdk_app_mesh.types.http_gateway_route_rewrite

        out["rewrite"] = (
            aws_sdk_app_mesh.types.http_gateway_route_rewrite.serialize_json(
                value["rewrite"]
            )
        )
    return out


def deserialize_json(data: dict) -> HttpGatewayRouteAction:
    out: HttpGatewayRouteAction = {}  # type: ignore[typeddict-item]
    if "target" in data:
        import aws_sdk_app_mesh.types.gateway_route_target

        out["target"] = aws_sdk_app_mesh.types.gateway_route_target.deserialize_json(
            data["target"]
        )
    else:
        raise DeserializationError("HttpGatewayRouteAction.target required")
    if "rewrite" in data:
        import aws_sdk_app_mesh.types.http_gateway_route_rewrite

        out["rewrite"] = (
            aws_sdk_app_mesh.types.http_gateway_route_rewrite.deserialize_json(
                data["rewrite"]
            )
        )
    return out
