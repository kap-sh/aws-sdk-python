"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#NotificationSettingKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.notification_channel
    import aws_sdk_rolesanywhere.types.notification_event


class NotificationSettingKey(TypedDict):
    event: "aws_sdk_rolesanywhere.types.notification_event.NotificationEvent"
    """<p>The notification setting event to reset.</p>"""
    channel: NotRequired[
        "aws_sdk_rolesanywhere.types.notification_channel.NotificationChannel"
    ]
    """<p>The specified channel of notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSettingKey) -> dict:
    out: dict = {}
    out["event"] = value["event"]
    if "channel" in value:
        out["channel"] = value["channel"]
    return out


def deserialize_json(data: dict) -> NotificationSettingKey:
    out: NotificationSettingKey = {}  # type: ignore[typeddict-item]
    if "event" in data:
        out["event"] = data["event"]
    else:
        raise DeserializationError("NotificationSettingKey.event required")
    if "channel" in data:
        out["channel"] = data["channel"]
    return out
