"""Generated from Smithy shape ``com.amazonaws.connect#NotificationSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.notification_search_criteria

NotificationSearchConditionList: TypeAlias = list[
    "capo_connect.types.notification_search_criteria.NotificationSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSearchConditionList) -> list:
    import capo_connect.types.notification_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.notification_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotificationSearchConditionList:
    import capo_connect.types.notification_search_criteria

    out: NotificationSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.notification_search_criteria.deserialize_json(item)
        )
    return out
