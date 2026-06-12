"""Generated from Smithy shape ``com.amazonaws.wickr#ListBotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.bot_status
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.sort_direction


class ListBotsRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which to list bots.</p>"""
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of bots to return in a single page. Valid range is 1-100. Default is 10.</p>"""
    sort_fields: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The fields to sort bots by. Multiple fields can be specified by separating them with '+'. Accepted values include 'username', 'firstName', 'displayName', 'status', and 'groupId'.</p>"""
    sort_direction: NotRequired["aws_sdk_wickr.types.sort_direction.SortDirection"]
    """<p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>"""
    display_name: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include bots with display names matching this value.</p>"""
    username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include bots with usernames matching this value.</p>"""
    status: NotRequired["aws_sdk_wickr.types.bot_status.BotStatus"]
    """<p>Filter results to only include bots with this status (1 for pending, 2 for active).</p>"""
    group_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include bots belonging to this security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBotsRequest:
    out: ListBotsRequest = {}  # type: ignore[typeddict-item]
    return out
