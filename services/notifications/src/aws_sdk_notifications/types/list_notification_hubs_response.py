"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationHubsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_hubs


class ListNotificationHubsResponse(TypedDict):
    notification_hubs: "aws_sdk_notifications.types.notification_hubs.NotificationHubs"
    """<p>The <code>NotificationHubs</code> in the account.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationHubsResponse) -> dict:
    out: dict = {}
    import aws_sdk_notifications.types.notification_hubs

    out["notificationHubs"] = (
        aws_sdk_notifications.types.notification_hubs.serialize_json(
            value["notification_hubs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationHubsResponse:
    out: ListNotificationHubsResponse = {}  # type: ignore[typeddict-item]
    if "notificationHubs" in data:
        import aws_sdk_notifications.types.notification_hubs

        out["notification_hubs"] = (
            aws_sdk_notifications.types.notification_hubs.deserialize_json(
                data["notificationHubs"]
            )
        )
    else:
        raise DeserializationError(
            "ListNotificationHubsResponse.notification_hubs required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
