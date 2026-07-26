"""Generated from Smithy shape ``com.amazonaws.networkmanager#DescribeGlobalNetworksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_list
    import capo_networkmanager.types.next_token


class DescribeGlobalNetworksResponse(TypedDict, closed=True):
    global_networks: NotRequired[
        "capo_networkmanager.types.global_network_list.GlobalNetworkList"
    ]
    """<p>Information about the global networks.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGlobalNetworksResponse) -> dict:
    out: dict = {}
    if "global_networks" in value:
        import capo_networkmanager.types.global_network_list

        out["GlobalNetworks"] = (
            capo_networkmanager.types.global_network_list.serialize_json(
                value["global_networks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeGlobalNetworksResponse:
    out: DescribeGlobalNetworksResponse = {}  # type: ignore[typeddict-item]
    if "GlobalNetworks" in data:
        import capo_networkmanager.types.global_network_list

        out["global_networks"] = (
            capo_networkmanager.types.global_network_list.deserialize_json(
                data["GlobalNetworks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
