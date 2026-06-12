"""Generated from Smithy shape ``com.amazonaws.connect#NotificationSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.notification_search_summary

NotificationSearchSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.notification_search_summary.NotificationSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSearchSummaryList) -> list:
    import aws_sdk_connect.types.notification_search_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.notification_search_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationSearchSummaryList:
    import aws_sdk_connect.types.notification_search_summary

    out: NotificationSearchSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.notification_search_summary.deserialize_json(item)
        )
    return out
