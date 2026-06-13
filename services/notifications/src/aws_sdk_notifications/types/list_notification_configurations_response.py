"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configurations


class ListNotificationConfigurationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    notification_configurations: "aws_sdk_notifications.types.notification_configurations.NotificationConfigurations"
    """<p>The <code>NotificationConfigurations</code> in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_notifications.types.notification_configurations

    out["notificationConfigurations"] = (
        aws_sdk_notifications.types.notification_configurations.serialize_json(
            value["notification_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListNotificationConfigurationsResponse:
    out: ListNotificationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "notificationConfigurations" in data:
        import aws_sdk_notifications.types.notification_configurations

        out["notification_configurations"] = (
            aws_sdk_notifications.types.notification_configurations.deserialize_json(
                data["notificationConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListNotificationConfigurationsResponse.notification_configurations required"
        )
    return out
