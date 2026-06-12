"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_notifications.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_events
    import aws_sdk_notifications.types.next_token

class ListManagedNotificationEventsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    managed_notification_events: "aws_sdk_notifications.types.managed_notification_events.ManagedNotificationEvents"
    """<p>A list of Managed Notification Events matching the request criteria.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_notifications.types.managed_notification_events
    out["managedNotificationEvents"] = aws_sdk_notifications.types.managed_notification_events.serialize_json(value["managed_notification_events"])
    return out


def deserialize_json(data: dict) -> ListManagedNotificationEventsResponse:
    out: ListManagedNotificationEventsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "managedNotificationEvents" in data:
        import aws_sdk_notifications.types.managed_notification_events
        out["managed_notification_events"] = aws_sdk_notifications.types.managed_notification_events.deserialize_json(data["managedNotificationEvents"])
    else:
        raise DeserializationError("ListManagedNotificationEventsResponse.managed_notification_events required")
    return out