"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.notification_output

NotificationsList: TypeAlias = list[
    "aws_sdk_datazone.types.notification_output.NotificationOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationsList) -> list:
    import aws_sdk_datazone.types.notification_output

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.notification_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotificationsList:
    import aws_sdk_datazone.types.notification_output

    out: NotificationsList = []
    for item in data:
        out.append(aws_sdk_datazone.types.notification_output.deserialize_json(item))
    return out
