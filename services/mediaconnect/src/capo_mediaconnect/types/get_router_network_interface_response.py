"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterNetworkInterfaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface


class GetRouterNetworkInterfaceResponse(TypedDict, closed=True):
    router_network_interface: (
        "capo_mediaconnect.types.router_network_interface.RouterNetworkInterface"
    )
    """<p>The details of the requested router network interface, including its configuration and other attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterNetworkInterfaceResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_network_interface

    out["routerNetworkInterface"] = (
        capo_mediaconnect.types.router_network_interface.serialize_json(
            value["router_network_interface"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRouterNetworkInterfaceResponse:
    out: GetRouterNetworkInterfaceResponse = {}  # type: ignore[typeddict-item]
    if "routerNetworkInterface" in data:
        import capo_mediaconnect.types.router_network_interface

        out["router_network_interface"] = (
            capo_mediaconnect.types.router_network_interface.deserialize_json(
                data["routerNetworkInterface"]
            )
        )
    else:
        raise DeserializationError(
            "GetRouterNetworkInterfaceResponse.router_network_interface required"
        )
    return out
