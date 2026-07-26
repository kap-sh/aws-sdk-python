"""Generated from Smithy shape ``com.amazonaws.notifications#RegisterNotificationHubResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.creation_time
    import capo_notifications.types.last_activation_time
    import capo_notifications.types.notification_hub_status_summary
    import capo_notifications.types.region


class RegisterNotificationHubResponse(TypedDict, closed=True):
    notification_hub_region: "capo_notifications.types.region.Region"
    """<p>The Region of the <code>NotificationHub</code>.</p>"""
    status_summary: "capo_notifications.types.notification_hub_status_summary.NotificationHubStatusSummary"
    """<p>Provides additional information about the current <code>NotificationConfiguration</code> status information.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The date the resource was created.</p>"""
    last_activation_time: NotRequired[
        "capo_notifications.types.last_activation_time.LastActivationTime"
    ]
    """<p>The date the resource was last activated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterNotificationHubResponse) -> dict:
    out: dict = {}
    out["notificationHubRegion"] = value["notification_hub_region"]
    import capo_notifications.types.notification_hub_status_summary

    out["statusSummary"] = (
        capo_notifications.types.notification_hub_status_summary.serialize_json(
            value["status_summary"]
        )
    )
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    if "last_activation_time" in value:
        import capo_notifications.types.last_activation_time

        out["lastActivationTime"] = (
            capo_notifications.types.last_activation_time.serialize_json(
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
        import capo_notifications.types.notification_hub_status_summary

        out["status_summary"] = (
            capo_notifications.types.notification_hub_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterNotificationHubResponse.status_summary required"
        )
    if "creationTime" in data:
        import capo_notifications.types.creation_time

        out["creation_time"] = capo_notifications.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "RegisterNotificationHubResponse.creation_time required"
        )
    if "lastActivationTime" in data:
        import capo_notifications.types.last_activation_time

        out["last_activation_time"] = (
            capo_notifications.types.last_activation_time.deserialize_json(
                data["lastActivationTime"]
            )
        )
    return out
