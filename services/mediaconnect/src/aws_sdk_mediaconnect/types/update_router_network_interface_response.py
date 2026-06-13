"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterNetworkInterfaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface


class UpdateRouterNetworkInterfaceResponse(TypedDict):
    router_network_interface: (
        "aws_sdk_mediaconnect.types.router_network_interface.RouterNetworkInterface"
    )
    """<p>The updated router network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterNetworkInterfaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_network_interface

    out["routerNetworkInterface"] = (
        aws_sdk_mediaconnect.types.router_network_interface.serialize_json(
            value["router_network_interface"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRouterNetworkInterfaceResponse:
    out: UpdateRouterNetworkInterfaceResponse = {}  # type: ignore[typeddict-item]
    if "routerNetworkInterface" in data:
        import aws_sdk_mediaconnect.types.router_network_interface

        out["router_network_interface"] = (
            aws_sdk_mediaconnect.types.router_network_interface.deserialize_json(
                data["routerNetworkInterface"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRouterNetworkInterfaceResponse.router_network_interface required"
        )
    return out
