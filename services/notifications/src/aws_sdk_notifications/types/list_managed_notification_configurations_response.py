"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_configurations
    import aws_sdk_notifications.types.next_token


class ListManagedNotificationConfigurationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    managed_notification_configurations: "aws_sdk_notifications.types.managed_notification_configurations.ManagedNotificationConfigurations"
    """<p>A list of Managed Notification Configurations matching the request criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_notifications.types.managed_notification_configurations

    out["managedNotificationConfigurations"] = (
        aws_sdk_notifications.types.managed_notification_configurations.serialize_json(
            value["managed_notification_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedNotificationConfigurationsResponse:
    out: ListManagedNotificationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "managedNotificationConfigurations" in data:
        import aws_sdk_notifications.types.managed_notification_configurations

        out["managed_notification_configurations"] = (
            aws_sdk_notifications.types.managed_notification_configurations.deserialize_json(
                data["managedNotificationConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListManagedNotificationConfigurationsResponse.managed_notification_configurations required"
        )
    return out
