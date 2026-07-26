"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetLinksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id_list
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.site_id


class GetLinksRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    link_ids: NotRequired["capo_networkmanager.types.link_id_list.LinkIdList"]
    """<p>One or more link IDs. The maximum is 10.</p>"""
    site_id: NotRequired["capo_networkmanager.types.site_id.SiteId"]
    """<p>The ID of the site.</p>"""
    type: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The link type.</p>"""
    provider: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The link provider.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLinksRequest:
    out: GetLinksRequest = {}  # type: ignore[typeddict-item]
    return out
