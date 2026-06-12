"""Generated from Smithy shape ``com.amazonaws.connect#NotificationPriority``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The priority level of a notification. Valid values are URGENT (reserved for system-generated notifications during availability or security events), HIGH, and LOW. High priority notifications are displayed above low priority notifications in the notification widget.</p>"""
NotificationPriority: TypeAlias = Literal[
    "URGENT",
    "HIGH",
    "LOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "URGENT",
        "HIGH",
        "LOW",
    )
)


def serialize_json(value: NotificationPriority) -> str:
    return value


def deserialize_json(data: str) -> NotificationPriority:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationPriority value: {data!r}")
    return cast(NotificationPriority, data)
