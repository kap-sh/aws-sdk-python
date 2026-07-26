"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationMessageTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.notification_message_type

NotificationMessageTypes: TypeAlias = list[
    "capo_devops_guru.types.notification_message_type.NotificationMessageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationMessageTypes) -> list:
    import capo_devops_guru.types.notification_message_type

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.notification_message_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationMessageTypes:
    import capo_devops_guru.types.notification_message_type

    out: NotificationMessageTypes = []
    for item in data:
        out.append(
            capo_devops_guru.types.notification_message_type.deserialize_json(item)
        )
    return out
