"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListNotificationRulesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_notifications.errors import DeserializationError

ListNotificationRulesFilterName: TypeAlias = Literal[
    "EVENT_TYPE_ID",
    "CREATED_BY",
    "RESOURCE",
    "TARGET_ADDRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENT_TYPE_ID",
        "CREATED_BY",
        "RESOURCE",
        "TARGET_ADDRESS",
    )
)


def serialize_json(value: ListNotificationRulesFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListNotificationRulesFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListNotificationRulesFilterName value: {data!r}"
        )
    return cast(ListNotificationRulesFilterName, data)
