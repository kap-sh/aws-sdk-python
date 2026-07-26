"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface_arn


class DeleteRouterNetworkInterfaceRequest(TypedDict, closed=True):
    arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the router network interface that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterNetworkInterfaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRouterNetworkInterfaceRequest:
    out: DeleteRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    return out
