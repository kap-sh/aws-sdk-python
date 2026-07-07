"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_events


class ListNotificationEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    notification_events: (
        "aws_sdk_notifications.types.notification_events.NotificationEvents"
    )
    """<p>The list of notification events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_notifications.types.notification_events

    out["notificationEvents"] = (
        aws_sdk_notifications.types.notification_events.serialize_json(
            value["notification_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListNotificationEventsResponse:
    out: ListNotificationEventsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "notificationEvents" in data:
        import aws_sdk_notifications.types.notification_events

        out["notification_events"] = (
            aws_sdk_notifications.types.notification_events.deserialize_json(
                data["notificationEvents"]
            )
        )
    else:
        raise DeserializationError(
            "ListNotificationEventsResponse.notification_events required"
        )
    return out
