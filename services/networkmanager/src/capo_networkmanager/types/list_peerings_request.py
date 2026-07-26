"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListPeeringsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.peering_state
    import capo_networkmanager.types.peering_type


class ListPeeringsRequest(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    peering_type: NotRequired["capo_networkmanager.types.peering_type.PeeringType"]
    """<p>Returns a list of a peering requests.</p>"""
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>Returns a list edge locations for the </p>"""
    state: NotRequired["capo_networkmanager.types.peering_state.PeeringState"]
    """<p>Returns a list of the peering request states.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPeeringsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPeeringsRequest:
    out: ListPeeringsRequest = {}  # type: ignore[typeddict-item]
    return out
