"""Generated from Smithy shape ``com.amazonaws.wickr#ListGuestUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.sort_direction


class ListGuestUsersRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which to list guest users.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of guest users to return in a single page. Valid range is 1-100. Default is 10.</p>"""
    sort_direction: NotRequired["aws_sdk_wickr.types.sort_direction.SortDirection"]
    """<p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>"""
    sort_fields: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The field to sort guest users by. Accepted values include 'username' and 'billingPeriod'.</p>"""
    username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include guest users with usernames matching this value.</p>"""
    billing_period: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include guest users from this billing period (e.g., '2024-01').</p>"""
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGuestUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGuestUsersRequest:
    out: ListGuestUsersRequest = {}  # type: ignore[typeddict-item]
    return out
