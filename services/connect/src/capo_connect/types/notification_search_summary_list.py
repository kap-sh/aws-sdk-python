"""Generated from Smithy shape ``com.amazonaws.connect#NotificationSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.notification_search_summary

NotificationSearchSummaryList: TypeAlias = list[
    "capo_connect.types.notification_search_summary.NotificationSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSearchSummaryList) -> list:
    import capo_connect.types.notification_search_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.notification_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotificationSearchSummaryList:
    import capo_connect.types.notification_search_summary

    out: NotificationSearchSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.notification_search_summary.deserialize_json(item)
        )
    return out
