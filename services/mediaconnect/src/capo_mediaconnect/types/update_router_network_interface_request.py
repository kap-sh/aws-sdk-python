"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.router_network_interface_configuration


class UpdateRouterNetworkInterfaceRequest(TypedDict, closed=True):
    arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the router network interface that you want to update.</p>"""
    name: NotRequired["str"]
    """<p>The updated name for the router network interface.</p>"""
    configuration: NotRequired[
        "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
    ]
    """<p>The updated configuration settings for the router network interface. Changing the type of the configuration is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterNetworkInterfaceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import capo_mediaconnect.types.router_network_interface_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_network_interface_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRouterNetworkInterfaceRequest:
    out: UpdateRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "configuration" in data:
        import capo_mediaconnect.types.router_network_interface_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_network_interface_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
