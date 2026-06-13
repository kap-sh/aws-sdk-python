"""Generated from Smithy shape ``com.amazonaws.grafana#NotificationDestinationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.notification_destination_type

NotificationDestinationsList: TypeAlias = list[
    "aws_sdk_grafana.types.notification_destination_type.NotificationDestinationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationDestinationsList) -> list:
    return list(value)


def deserialize_json(data: list) -> NotificationDestinationsList:
    return list(data)
