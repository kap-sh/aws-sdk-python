"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_summary_list
    import aws_sdk_networkmanager.types.next_token


class ListCoreNetworksResponse(TypedDict, closed=True):
    core_networks: NotRequired[
        "aws_sdk_networkmanager.types.core_network_summary_list.CoreNetworkSummaryList"
    ]
    """<p>Describes the list of core networks.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworksResponse) -> dict:
    out: dict = {}
    if "core_networks" in value:
        import aws_sdk_networkmanager.types.core_network_summary_list

        out["CoreNetworks"] = (
            aws_sdk_networkmanager.types.core_network_summary_list.serialize_json(
                value["core_networks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoreNetworksResponse:
    out: ListCoreNetworksResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworks" in data:
        import aws_sdk_networkmanager.types.core_network_summary_list

        out["core_networks"] = (
            aws_sdk_networkmanager.types.core_network_summary_list.deserialize_json(
                data["CoreNetworks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
