"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkPrefixListAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.prefix_list_arn


class ListCoreNetworkPrefixListAssociationsRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network to list prefix list associations for.</p>"""
    prefix_list_arn: NotRequired[
        "capo_networkmanager.types.prefix_list_arn.PrefixListArn"
    ]
    """<p>The ARN of a specific prefix list to filter the associations.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single page.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkPrefixListAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCoreNetworkPrefixListAssociationsRequest:
    out: ListCoreNetworkPrefixListAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
