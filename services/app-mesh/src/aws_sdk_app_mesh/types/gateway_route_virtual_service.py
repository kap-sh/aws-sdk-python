"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteVirtualService``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.resource_name


class GatewayRouteVirtualService(TypedDict):
    virtual_service_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual service that traffic is routed to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteVirtualService) -> dict:
    out: dict = {}
    out["virtualServiceName"] = value["virtual_service_name"]
    return out


def deserialize_json(data: dict) -> GatewayRouteVirtualService:
    out: GatewayRouteVirtualService = {}  # type: ignore[typeddict-item]
    if "virtualServiceName" in data:
        out["virtual_service_name"] = data["virtualServiceName"]
    else:
        raise DeserializationError(
            "GatewayRouteVirtualService.virtual_service_name required"
        )
    return out
