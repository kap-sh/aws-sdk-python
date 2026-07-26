"""Generated from Smithy shape ``com.amazonaws.connect#NotificationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a notification for a specific user. Valid values are READ, UNREAD, and HIDDEN (removes the notification from the widget).</p>"""
NotificationStatus: TypeAlias = Literal[
    "READ",
    "UNREAD",
    "HIDDEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationStatus) -> str:
    return value


def deserialize_json(data: str) -> NotificationStatus:
    return cast(NotificationStatus, data)
