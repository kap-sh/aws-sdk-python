"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_status_code


class GatewayRouteStatus(TypedDict):
    status: "aws_sdk_app_mesh.types.gateway_route_status_code.GatewayRouteStatusCode"
    """<p>The current status for the gateway route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> GatewayRouteStatus:
    out: GatewayRouteStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GatewayRouteStatus.status required")
    return out
