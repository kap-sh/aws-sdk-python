"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationMessageTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.notification_message_type

NotificationMessageTypes: TypeAlias = list[
    "aws_sdk_devops_guru.types.notification_message_type.NotificationMessageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationMessageTypes) -> list:
    import aws_sdk_devops_guru.types.notification_message_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.notification_message_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationMessageTypes:
    import aws_sdk_devops_guru.types.notification_message_type

    out: NotificationMessageTypes = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.notification_message_type.deserialize_json(item)
        )
    return out
