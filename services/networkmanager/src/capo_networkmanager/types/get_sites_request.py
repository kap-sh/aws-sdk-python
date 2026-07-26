"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetSitesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.site_id_list


class GetSitesRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    site_ids: NotRequired["capo_networkmanager.types.site_id_list.SiteIdList"]
    """<p>One or more site IDs. The maximum is 10.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSitesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSitesRequest:
    out: GetSitesRequest = {}  # type: ignore[typeddict-item]
    return out
