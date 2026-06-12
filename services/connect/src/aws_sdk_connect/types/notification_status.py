"""Generated from Smithy shape ``com.amazonaws.connect#NotificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The status of a notification for a specific user. Valid values are READ, UNREAD, and HIDDEN (removes the notification from the widget).</p>"""
NotificationStatus: TypeAlias = Literal[
    "READ",
    "UNREAD",
    "HIDDEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "UNREAD",
        "HIDDEN",
    )
)


def serialize_json(value: NotificationStatus) -> str:
    return value


def deserialize_json(data: str) -> NotificationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationStatus value: {data!r}")
    return cast(NotificationStatus, data)
