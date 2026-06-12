"""Generated from Smithy shape ``com.amazonaws.wickr#ListUsersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.sensitive_string
    import aws_sdk_wickr.types.sort_direction
    import aws_sdk_wickr.types.user_status


class ListUsersRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which to list users.</p>"""
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of users to return in a single page. Valid range is 1-100. Default is 10.</p>"""
    sort_fields: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The fields to sort users by. Multiple fields can be specified by separating them with '+'. Accepted values include 'username', 'firstName', 'lastName', 'status', and 'groupId'.</p>"""
    sort_direction: NotRequired["aws_sdk_wickr.types.sort_direction.SortDirection"]
    """<p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>"""
    first_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>Filter results to only include users with first names matching this value.</p>"""
    last_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>Filter results to only include users with last names matching this value.</p>"""
    username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include users with usernames matching this value.</p>"""
    status: NotRequired["aws_sdk_wickr.types.user_status.UserStatus"]
    """<p>Filter results to only include users with this status (1 for pending, 2 for active).</p>"""
    group_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include users belonging to this security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUsersRequest:
    out: ListUsersRequest = {}  # type: ignore[typeddict-item]
    return out
