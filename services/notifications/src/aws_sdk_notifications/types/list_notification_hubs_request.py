"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationHubsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_notifications.types.next_token

class ListNotificationHubsRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of records to list in a single response.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. Set to null to start listing notification hubs from the start.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationHubsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotificationHubsRequest:
    out: ListNotificationHubsRequest = {}  # type: ignore[typeddict-item]
    return out