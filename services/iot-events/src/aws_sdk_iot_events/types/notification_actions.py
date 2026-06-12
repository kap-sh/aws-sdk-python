"""Generated from Smithy shape ``com.amazonaws.iotevents#NotificationActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.notification_action

NotificationActions: TypeAlias = list[
    "aws_sdk_iot_events.types.notification_action.NotificationAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationActions) -> list:
    import aws_sdk_iot_events.types.notification_action

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.notification_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotificationActions:
    import aws_sdk_iot_events.types.notification_action

    out: NotificationActions = []
    for item in data:
        out.append(aws_sdk_iot_events.types.notification_action.deserialize_json(item))
    return out
