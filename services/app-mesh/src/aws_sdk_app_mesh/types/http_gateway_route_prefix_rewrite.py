"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpGatewayRoutePrefixRewrite``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.default_gateway_route_rewrite
    import aws_sdk_app_mesh.types.http_gateway_route_prefix


class HttpGatewayRoutePrefixRewrite(TypedDict, closed=True):
    default_prefix: NotRequired[
        "aws_sdk_app_mesh.types.default_gateway_route_rewrite.DefaultGatewayRouteRewrite"
    ]
    """<p>The default prefix used to replace the incoming route prefix when rewritten.</p>"""
    value: NotRequired[
        "aws_sdk_app_mesh.types.http_gateway_route_prefix.HttpGatewayRoutePrefix"
    ]
    """<p>The value used to replace the incoming route prefix when rewritten.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpGatewayRoutePrefixRewrite) -> dict:
    out: dict = {}
    if "default_prefix" in value:
        out["defaultPrefix"] = value["default_prefix"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> HttpGatewayRoutePrefixRewrite:
    out: HttpGatewayRoutePrefixRewrite = {}  # type: ignore[typeddict-item]
    if "defaultPrefix" in data:
        out["default_prefix"] = data["defaultPrefix"]
    if "value" in data:
        out["value"] = data["value"]
    return out
