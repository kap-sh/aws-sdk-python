"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterNetworkInterfaceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_mediaconnect.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.batch_get_router_network_interface_error_list
    import aws_sdk_mediaconnect.types.router_network_interface_list

class BatchGetRouterNetworkInterfaceResponse(TypedDict):
    router_network_interfaces: "aws_sdk_mediaconnect.types.router_network_interface_list.RouterNetworkInterfaceList"
    """<p>An array of router network interfaces that were successfully retrieved.</p>"""
    errors: "aws_sdk_mediaconnect.types.batch_get_router_network_interface_error_list.BatchGetRouterNetworkInterfaceErrorList"
    """<p>An array of errors that occurred when retrieving the requested router network interfaces.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterNetworkInterfaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_network_interface_list
    out["routerNetworkInterfaces"] = aws_sdk_mediaconnect.types.router_network_interface_list.serialize_json(value["router_network_interfaces"])
    import aws_sdk_mediaconnect.types.batch_get_router_network_interface_error_list
    out["errors"] = aws_sdk_mediaconnect.types.batch_get_router_network_interface_error_list.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchGetRouterNetworkInterfaceResponse:
    out: BatchGetRouterNetworkInterfaceResponse = {}  # type: ignore[typeddict-item]
    if "routerNetworkInterfaces" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_list
        out["router_network_interfaces"] = aws_sdk_mediaconnect.types.router_network_interface_list.deserialize_json(data["routerNetworkInterfaces"])
    else:
        raise DeserializationError("BatchGetRouterNetworkInterfaceResponse.router_network_interfaces required")
    if "errors" in data:
        import aws_sdk_mediaconnect.types.batch_get_router_network_interface_error_list
        out["errors"] = aws_sdk_mediaconnect.types.batch_get_router_network_interface_error_list.deserialize_json(data["errors"])
    else:
        raise DeserializationError("BatchGetRouterNetworkInterfaceResponse.errors required")
    return out