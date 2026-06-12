"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationChannel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.notification_channel_config
    import aws_sdk_devops_guru.types.notification_channel_id


class NotificationChannel(TypedDict):
    id: NotRequired[
        "aws_sdk_devops_guru.types.notification_channel_id.NotificationChannelId"
    ]
    """<p> The ID of a notification channel. </p>"""
    config: NotRequired[
        "aws_sdk_devops_guru.types.notification_channel_config.NotificationChannelConfig"
    ]
    """<p> A <code>NotificationChannelConfig</code> object that contains information about configured notification channels. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationChannel) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "config" in value:
        import aws_sdk_devops_guru.types.notification_channel_config

        out["Config"] = (
            aws_sdk_devops_guru.types.notification_channel_config.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationChannel:
    out: NotificationChannel = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Config" in data:
        import aws_sdk_devops_guru.types.notification_channel_config

        out["config"] = (
            aws_sdk_devops_guru.types.notification_channel_config.deserialize_json(
                data["Config"]
            )
        )
    return out
