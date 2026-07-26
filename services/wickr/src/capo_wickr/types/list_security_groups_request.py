"""Generated from Smithy shape ``com.amazonaws.wickr#ListSecurityGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.sort_direction


class ListSecurityGroupsRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which to list security groups.</p>"""
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of security groups to return in a single page. Valid range is 1-100. Default is 10.</p>"""
    sort_fields: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The field to sort security groups by. Accepted values include 'id' and 'name'.</p>"""
    sort_direction: NotRequired["capo_wickr.types.sort_direction.SortDirection"]
    """<p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSecurityGroupsRequest:
    out: ListSecurityGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
