"""Generated from Smithy shape ``com.amazonaws.devopsguru#AddNotificationChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_guru.types.notification_channel_config


class AddNotificationChannelRequest(TypedDict, closed=True):
    config: (
        "capo_devops_guru.types.notification_channel_config.NotificationChannelConfig"
    )
    """<p> A <code>NotificationChannelConfig</code> object that specifies what type of notification channel to add. The one supported notification channel is Amazon Simple Notification Service (Amazon SNS). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddNotificationChannelRequest) -> dict:
    out: dict = {}
    import capo_devops_guru.types.notification_channel_config

    out["Config"] = capo_devops_guru.types.notification_channel_config.serialize_json(
        value["config"]
    )
    return out


def deserialize_json(data: dict) -> AddNotificationChannelRequest:
    out: AddNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    if "Config" in data:
        import capo_devops_guru.types.notification_channel_config

        out["config"] = (
            capo_devops_guru.types.notification_channel_config.deserialize_json(
                data["Config"]
            )
        )
    else:
        raise DeserializationError("AddNotificationChannelRequest.config required")
    return out
