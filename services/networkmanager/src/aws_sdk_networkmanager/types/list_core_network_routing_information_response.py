"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkRoutingInformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_routing_information_list
    import aws_sdk_networkmanager.types.next_token


class ListCoreNetworkRoutingInformationResponse(TypedDict, closed=True):
    core_network_routing_information: NotRequired[
        "aws_sdk_networkmanager.types.core_network_routing_information_list.CoreNetworkRoutingInformationList"
    ]
    """<p>The list of routing information for the core network.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkRoutingInformationResponse) -> dict:
    out: dict = {}
    if "core_network_routing_information" in value:
        import aws_sdk_networkmanager.types.core_network_routing_information_list

        out["CoreNetworkRoutingInformation"] = (
            aws_sdk_networkmanager.types.core_network_routing_information_list.serialize_json(
                value["core_network_routing_information"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoreNetworkRoutingInformationResponse:
    out: ListCoreNetworkRoutingInformationResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkRoutingInformation" in data:
        import aws_sdk_networkmanager.types.core_network_routing_information_list

        out["core_network_routing_information"] = (
            aws_sdk_networkmanager.types.core_network_routing_information_list.deserialize_json(
                data["CoreNetworkRoutingInformation"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
