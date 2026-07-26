"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetLinkAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class GetLinkAssociationsRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: NotRequired["capo_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLinkAssociationsRequest:
    out: GetLinkAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
