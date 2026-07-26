"""Generated from Smithy shape ``com.amazonaws.connect#UserNotificationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.user_notification_summary

UserNotificationSummaryList: TypeAlias = list[
    "capo_connect.types.user_notification_summary.UserNotificationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserNotificationSummaryList) -> list:
    import capo_connect.types.user_notification_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.user_notification_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserNotificationSummaryList:
    import capo_connect.types.user_notification_summary

    out: UserNotificationSummaryList = []
    for item in data:
        out.append(capo_connect.types.user_notification_summary.deserialize_json(item))
    return out
