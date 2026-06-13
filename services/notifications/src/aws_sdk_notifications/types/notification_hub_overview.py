"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationHubOverview``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.creation_time
    import aws_sdk_notifications.types.last_activation_time
    import aws_sdk_notifications.types.notification_hub_status_summary
    import aws_sdk_notifications.types.region


class NotificationHubOverview(TypedDict):
    notification_hub_region: "aws_sdk_notifications.types.region.Region"
    """<p>The Region of the resource.</p>"""
    status_summary: "aws_sdk_notifications.types.notification_hub_status_summary.NotificationHubStatusSummary"
    """<p>The status summary of the resource.</p>"""
    creation_time: "aws_sdk_notifications.types.creation_time.CreationTime"
    """<p>The date and time the <code>NotificationHubOverview</code> was created.</p>"""
    last_activation_time: NotRequired[
        "aws_sdk_notifications.types.last_activation_time.LastActivationTime"
    ]
    """<p>The most recent time this <code>NotificationHub</code> had an <code>ACTIVE</code> status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationHubOverview) -> dict:
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


def deserialize_json(data: dict) -> NotificationHubOverview:
    out: NotificationHubOverview = {}  # type: ignore[typeddict-item]
    if "notificationHubRegion" in data:
        out["notification_hub_region"] = data["notificationHubRegion"]
    else:
        raise DeserializationError(
            "NotificationHubOverview.notification_hub_region required"
        )
    if "statusSummary" in data:
        import aws_sdk_notifications.types.notification_hub_status_summary

        out["status_summary"] = (
            aws_sdk_notifications.types.notification_hub_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    else:
        raise DeserializationError("NotificationHubOverview.status_summary required")
    if "creationTime" in data:
        import aws_sdk_notifications.types.creation_time

        out["creation_time"] = (
            aws_sdk_notifications.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("NotificationHubOverview.creation_time required")
    if "lastActivationTime" in data:
        import aws_sdk_notifications.types.last_activation_time

        out["last_activation_time"] = (
            aws_sdk_notifications.types.last_activation_time.deserialize_json(
                data["lastActivationTime"]
            )
        )
    return out
