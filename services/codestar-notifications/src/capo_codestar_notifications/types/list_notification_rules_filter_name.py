"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListNotificationRulesFilterName``."""

from typing import Literal, TypeAlias, cast

ListNotificationRulesFilterName: TypeAlias = Literal[
    "EVENT_TYPE_ID",
    "CREATED_BY",
    "RESOURCE",
    "TARGET_ADDRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationRulesFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListNotificationRulesFilterName:
    return cast(ListNotificationRulesFilterName, data)
