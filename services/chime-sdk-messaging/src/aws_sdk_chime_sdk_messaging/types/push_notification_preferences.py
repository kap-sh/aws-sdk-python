"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PushNotificationPreferences``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.allow_notifications
    import aws_sdk_chime_sdk_messaging.types.filter_rule


class PushNotificationPreferences(TypedDict):
    allow_notifications: (
        "aws_sdk_chime_sdk_messaging.types.allow_notifications.AllowNotifications"
    )
    """<p>Enum value that indicates which push notifications to send to the requested member of a channel. <code>ALL</code> sends all push notifications, <code>NONE</code> sends no push notifications, <code>FILTERED</code> sends only filtered push notifications. </p>"""
    filter_rule: NotRequired["aws_sdk_chime_sdk_messaging.types.filter_rule.FilterRule"]
    """<p>The simple JSON object used to send a subset of a push notification to the requested member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationPreferences) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_messaging.types.allow_notifications

    out["AllowNotifications"] = (
        aws_sdk_chime_sdk_messaging.types.allow_notifications.serialize_json(
            value["allow_notifications"]
        )
    )
    if "filter_rule" in value:
        out["FilterRule"] = value["filter_rule"]
    return out


def deserialize_json(data: dict) -> PushNotificationPreferences:
    out: PushNotificationPreferences = {}  # type: ignore[typeddict-item]
    if "AllowNotifications" in data:
        import aws_sdk_chime_sdk_messaging.types.allow_notifications

        out["allow_notifications"] = (
            aws_sdk_chime_sdk_messaging.types.allow_notifications.deserialize_json(
                data["AllowNotifications"]
            )
        )
    else:
        raise DeserializationError(
            "PushNotificationPreferences.allow_notifications required"
        )
    if "FilterRule" in data:
        out["filter_rule"] = data["FilterRule"]
    return out
