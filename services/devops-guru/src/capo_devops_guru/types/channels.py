"""Generated from Smithy shape ``com.amazonaws.devopsguru#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.notification_channel

Channels: TypeAlias = list[
    "capo_devops_guru.types.notification_channel.NotificationChannel"
]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    import capo_devops_guru.types.notification_channel

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.notification_channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> Channels:
    import capo_devops_guru.types.notification_channel

    out: Channels = []
    for item in data:
        out.append(capo_devops_guru.types.notification_channel.deserialize_json(item))
    return out
