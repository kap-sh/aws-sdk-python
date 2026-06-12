"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface_arn_list

class BatchGetRouterNetworkInterfaceRequest(TypedDict):
    arns: "aws_sdk_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList"
    """<p>The Amazon Resource Names (ARNs) of the router network interfaces you want to retrieve information about.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterNetworkInterfaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetRouterNetworkInterfaceRequest:
    out: BatchGetRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    return out