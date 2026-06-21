"""Generated from Smithy shape ``com.amazonaws.connect#NotificationPriority``."""

from typing import Literal, TypeAlias, cast

"""<p>The priority level of a notification. Valid values are URGENT (reserved for system-generated notifications during availability or security events), HIGH, and LOW. High priority notifications are displayed above low priority notifications in the notification widget.</p>"""
NotificationPriority: TypeAlias = Literal[
    "URGENT",
    "HIGH",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationPriority) -> str:
    return value


def deserialize_json(data: str) -> NotificationPriority:
    return cast(NotificationPriority, data)
