"""Generated from Smithy shape ``com.amazonaws.notifications#DeregisterNotificationHubResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.notification_hub_status_summary
    import aws_sdk_notifications.types.region


class DeregisterNotificationHubResponse(TypedDict, closed=True):
    notification_hub_region: "aws_sdk_notifications.types.region.Region"
    """<p>The <code>NotificationConfiguration</code> Region.</p>"""
    status_summary: "aws_sdk_notifications.types.notification_hub_status_summary.NotificationHubStatusSummary"
    """<p> <code>NotificationConfiguration</code> status information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterNotificationHubResponse) -> dict:
    out: dict = {}
    out["notificationHubRegion"] = value["notification_hub_region"]
    import aws_sdk_notifications.types.notification_hub_status_summary

    out["statusSummary"] = (
        aws_sdk_notifications.types.notification_hub_status_summary.serialize_json(
            value["status_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeregisterNotificationHubResponse:
    out: DeregisterNotificationHubResponse = {}  # type: ignore[typeddict-item]
    if "notificationHubRegion" in data:
        out["notification_hub_region"] = data["notificationHubRegion"]
    else:
        raise DeserializationError(
            "DeregisterNotificationHubResponse.notification_hub_region required"
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
            "DeregisterNotificationHubResponse.status_summary required"
        )
    return out
