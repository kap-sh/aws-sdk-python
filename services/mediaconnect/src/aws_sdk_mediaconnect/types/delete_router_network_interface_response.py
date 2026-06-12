"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterNetworkInterfaceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_mediaconnect.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface_arn
    import aws_sdk_mediaconnect.types.router_network_interface_state

class DeleteRouterNetworkInterfaceResponse(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    """<p>The ARN of the deleted router network interface.</p>"""
    name: "str"
    """<p>The name of the deleted router network interface.</p>"""
    state: "aws_sdk_mediaconnect.types.router_network_interface_state.RouterNetworkInterfaceState"
    """<p>The current state of the deleted router network interface, indicating where it is in the deletion process.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterNetworkInterfaceResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_network_interface_state
    out["state"] = aws_sdk_mediaconnect.types.router_network_interface_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> DeleteRouterNetworkInterfaceResponse:
    out: DeleteRouterNetworkInterfaceResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteRouterNetworkInterfaceResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteRouterNetworkInterfaceResponse.name required")
    if "state" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_state
        out["state"] = aws_sdk_mediaconnect.types.router_network_interface_state.deserialize_json(data["state"])
    else:
        raise DeserializationError("DeleteRouterNetworkInterfaceResponse.state required")
    return out