"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_virtual_service
    import aws_sdk_app_mesh.types.listener_port


class GatewayRouteTarget(TypedDict, closed=True):
    virtual_service: "aws_sdk_app_mesh.types.gateway_route_virtual_service.GatewayRouteVirtualService"
    """<p>An object that represents a virtual service gateway route target.</p>"""
    port: NotRequired["aws_sdk_app_mesh.types.listener_port.ListenerPort"]
    """<p>The port number of the gateway route target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteTarget) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.gateway_route_virtual_service

    out["virtualService"] = (
        aws_sdk_app_mesh.types.gateway_route_virtual_service.serialize_json(
            value["virtual_service"]
        )
    )
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> GatewayRouteTarget:
    out: GatewayRouteTarget = {}  # type: ignore[typeddict-item]
    if "virtualService" in data:
        import aws_sdk_app_mesh.types.gateway_route_virtual_service

        out["virtual_service"] = (
            aws_sdk_app_mesh.types.gateway_route_virtual_service.deserialize_json(
                data["virtualService"]
            )
        )
    else:
        raise DeserializationError("GatewayRouteTarget.virtual_service required")
    if "port" in data:
        out["port"] = data["port"]
    return out
