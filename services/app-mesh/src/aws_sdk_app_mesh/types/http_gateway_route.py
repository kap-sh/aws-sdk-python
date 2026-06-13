"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpGatewayRoute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.http_gateway_route_action
    import aws_sdk_app_mesh.types.http_gateway_route_match


class HttpGatewayRoute(TypedDict):
    match: "aws_sdk_app_mesh.types.http_gateway_route_match.HttpGatewayRouteMatch"
    """<p>An object that represents the criteria for determining a request match.</p>"""
    action: "aws_sdk_app_mesh.types.http_gateway_route_action.HttpGatewayRouteAction"
    """<p>An object that represents the action to take if a match is determined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpGatewayRoute) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.http_gateway_route_match

    out["match"] = aws_sdk_app_mesh.types.http_gateway_route_match.serialize_json(
        value["match"]
    )
    import aws_sdk_app_mesh.types.http_gateway_route_action

    out["action"] = aws_sdk_app_mesh.types.http_gateway_route_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> HttpGatewayRoute:
    out: HttpGatewayRoute = {}  # type: ignore[typeddict-item]
    if "match" in data:
        import aws_sdk_app_mesh.types.http_gateway_route_match

        out["match"] = aws_sdk_app_mesh.types.http_gateway_route_match.deserialize_json(
            data["match"]
        )
    else:
        raise DeserializationError("HttpGatewayRoute.match required")
    if "action" in data:
        import aws_sdk_app_mesh.types.http_gateway_route_action

        out["action"] = (
            aws_sdk_app_mesh.types.http_gateway_route_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("HttpGatewayRoute.action required")
    return out
