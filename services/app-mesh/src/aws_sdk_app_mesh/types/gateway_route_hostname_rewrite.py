"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteHostnameRewrite``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.default_gateway_route_rewrite

class GatewayRouteHostnameRewrite(TypedDict):
    default_target_hostname: NotRequired["aws_sdk_app_mesh.types.default_gateway_route_rewrite.DefaultGatewayRouteRewrite"]
    """<p>The default target host name to write to.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteHostnameRewrite) -> dict:
    out: dict = {}
    if "default_target_hostname" in value:
        out["defaultTargetHostname"] = value["default_target_hostname"]
    return out


def deserialize_json(data: dict) -> GatewayRouteHostnameRewrite:
    out: GatewayRouteHostnameRewrite = {}  # type: ignore[typeddict-item]
    if "defaultTargetHostname" in data:
        out["default_target_hostname"] = data["defaultTargetHostname"]
    return out