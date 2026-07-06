"""Generated from Smithy shape ``com.amazonaws.wickr#ListDevicesForUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.sort_direction
    import aws_sdk_wickr.types.user_id


class ListDevicesForUserRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the user.</p>"""
    user_id: "aws_sdk_wickr.types.user_id.UserId"
    """<p>The unique identifier of the user whose devices will be listed.</p>"""
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of devices to return in a single page. Valid range is 1-100. Default is 10.</p>"""
    sort_fields: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The fields to sort devices by. Multiple fields can be specified by separating them with '+'. Accepted values include 'lastlogin', 'type', 'suspend', and 'created'.</p>"""
    sort_direction: NotRequired["aws_sdk_wickr.types.sort_direction.SortDirection"]
    """<p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesForUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDevicesForUserRequest:
    out: ListDevicesForUserRequest = {}  # type: ignore[typeddict-item]
    return out
