"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectPeerAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_id_list
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class GetConnectPeerAssociationsRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    connect_peer_ids: NotRequired[
        "capo_networkmanager.types.connect_peer_id_list.ConnectPeerIdList"
    ]
    """<p>The IDs of the Connect peers.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectPeerAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectPeerAssociationsRequest:
    out: GetConnectPeerAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
