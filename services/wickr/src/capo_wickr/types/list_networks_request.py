"""Generated from Smithy shape ``com.amazonaws.wickr#ListNetworksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.sort_direction


class ListNetworksRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of networks to return in a single page. Valid range is 1-100. Default is 10.</p>"""
    sort_fields: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The field to sort networks by. Accepted values are 'networkId' and 'networkName'. Default is 'networkId'.</p>"""
    sort_direction: NotRequired["capo_wickr.types.sort_direction.SortDirection"]
    """<p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>"""
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNetworksRequest:
    out: ListNetworksRequest = {}  # type: ignore[typeddict-item]
    return out
