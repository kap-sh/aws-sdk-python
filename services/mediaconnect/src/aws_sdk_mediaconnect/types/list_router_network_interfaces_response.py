"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterNetworkInterfacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_router_network_interface_list


class ListRouterNetworkInterfacesResponse(TypedDict, closed=True):
    router_network_interfaces: "aws_sdk_mediaconnect.types.listed_router_network_interface_list.ListedRouterNetworkInterfaceList"
    """<p>The summary information for the retrieved router network interfaces.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterNetworkInterfacesResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.listed_router_network_interface_list

    out["routerNetworkInterfaces"] = (
        aws_sdk_mediaconnect.types.listed_router_network_interface_list.serialize_json(
            value["router_network_interfaces"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRouterNetworkInterfacesResponse:
    out: ListRouterNetworkInterfacesResponse = {}  # type: ignore[typeddict-item]
    if "routerNetworkInterfaces" in data:
        import aws_sdk_mediaconnect.types.listed_router_network_interface_list

        out["router_network_interfaces"] = (
            aws_sdk_mediaconnect.types.listed_router_network_interface_list.deserialize_json(
                data["routerNetworkInterfaces"]
            )
        )
    else:
        raise DeserializationError(
            "ListRouterNetworkInterfacesResponse.router_network_interfaces required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
