"""Generated from Smithy shape ``com.amazonaws.connect#NotificationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.notification

NotificationSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.notification.Notification"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSummaryList) -> list:
    import aws_sdk_connect.types.notification

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.notification.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotificationSummaryList:
    import aws_sdk_connect.types.notification

    out: NotificationSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.notification.deserialize_json(item))
    return out
