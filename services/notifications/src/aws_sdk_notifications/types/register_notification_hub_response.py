"""Generated from Smithy shape ``com.amazonaws.notifications#RegisterNotificationHubResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.creation_time
    import aws_sdk_notifications.types.last_activation_time
    import aws_sdk_notifications.types.notification_hub_status_summary
    import aws_sdk_notifications.types.region


class RegisterNotificationHubResponse(TypedDict, closed=True):
    notification_hub_region: "aws_sdk_notifications.types.region.Region"
    """<p>The Region of the <code>NotificationHub</code>.</p>"""
    status_summary: "aws_sdk_notifications.types.notification_hub_status_summary.NotificationHubStatusSummary"
    """<p>Provides additional information about the current <code>NotificationConfiguration</code> status information.</p>"""
    creation_time: "aws_sdk_notifications.types.creation_time.CreationTime"
    """<p>The date the resource was created.</p>"""
    last_activation_time: NotRequired[
        "aws_sdk_notifications.types.last_activation_time.LastActivationTime"
    ]
    """<p>The date the resource was last activated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterNotificationHubResponse) -> dict:
    out: dict = {}
    out["notificationHubRegion"] = value["notification_hub_region"]
    import aws_sdk_notifications.types.notification_hub_status_summary

    out["statusSummary"] = (
        aws_sdk_notifications.types.notification_hub_status_summary.serialize_json(
            value["status_summary"]
        )
    )
    import aws_sdk_notifications.types.creation_time

    out["creationTime"] = aws_sdk_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    if "last_activation_time" in value:
        import aws_sdk_notifications.types.last_activation_time

        out["lastActivationTime"] = (
            aws_sdk_notifications.types.last_activation_time.serialize_json(
                value["last_activation_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterNotificationHubResponse:
    out: RegisterNotificationHubResponse = {}  # type: ignore[typeddict-item]
    if "notificationHubRegion" in data:
        out["notification_hub_region"] = data["notificationHubRegion"]
    else:
        raise DeserializationError(
            "RegisterNotificationHubResponse.notification_hub_region required"
        )
    if "statusSummary" in data:
        import aws_sdk_notifications.types.notification_hub_status_summary

        out["status_summary"] = (
            aws_sdk_notifications.types.notification_hub_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterNotificationHubResponse.status_summary required"
        )
    if "creationTime" in data:
        import aws_sdk_notifications.types.creation_time

        out["creation_time"] = (
            aws_sdk_notifications.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterNotificationHubResponse.creation_time required"
        )
    if "lastActivationTime" in data:
        import aws_sdk_notifications.types.last_activation_time

        out["last_activation_time"] = (
            aws_sdk_notifications.types.last_activation_time.deserialize_json(
                data["lastActivationTime"]
            )
        )
    return out
