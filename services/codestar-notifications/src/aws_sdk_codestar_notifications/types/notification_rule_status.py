"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#NotificationRuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_notifications.errors import DeserializationError

NotificationRuleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: NotificationRuleStatus) -> str:
    return value


def deserialize_json(data: str) -> NotificationRuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationRuleStatus value: {data!r}")
    return cast(NotificationRuleStatus, data)
