"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface_arn


class GetRouterNetworkInterfaceRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    """<p>The Amazon Resource Name (ARN) of the router network interface that you want to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterNetworkInterfaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouterNetworkInterfaceRequest:
    out: GetRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    return out
