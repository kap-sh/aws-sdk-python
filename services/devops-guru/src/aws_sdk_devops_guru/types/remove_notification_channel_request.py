"""Generated from Smithy shape ``com.amazonaws.devopsguru#RemoveNotificationChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.notification_channel_id


class RemoveNotificationChannelRequest(TypedDict):
    id: "aws_sdk_devops_guru.types.notification_channel_id.NotificationChannelId"
    """<p> The ID of the notification channel to be removed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveNotificationChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveNotificationChannelRequest:
    out: RemoveNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    return out
