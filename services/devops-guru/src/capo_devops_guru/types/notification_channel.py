"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.notification_channel_config
    import capo_devops_guru.types.notification_channel_id


class NotificationChannel(TypedDict, closed=True):
    id: NotRequired[
        "capo_devops_guru.types.notification_channel_id.NotificationChannelId"
    ]
    """<p> The ID of a notification channel. </p>"""
    config: NotRequired[
        "capo_devops_guru.types.notification_channel_config.NotificationChannelConfig"
    ]
    """<p> A <code>NotificationChannelConfig</code> object that contains information about configured notification channels. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationChannel) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "config" in value:
        import capo_devops_guru.types.notification_channel_config

        out["Config"] = (
            capo_devops_guru.types.notification_channel_config.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationChannel:
    out: NotificationChannel = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Config" in data:
        import capo_devops_guru.types.notification_channel_config

        out["config"] = (
            capo_devops_guru.types.notification_channel_config.deserialize_json(
                data["Config"]
            )
        )
    return out
