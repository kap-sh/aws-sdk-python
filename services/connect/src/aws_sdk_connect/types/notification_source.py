"""Generated from Smithy shape ``com.amazonaws.connect#NotificationSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The source that created the notification. Possible values include CUSTOMER (user-created), RULES (rule-generated), and SYSTEM (system-generated).</p>"""
NotificationSource: TypeAlias = Literal[
    "CUSTOMER",
    "RULES",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSource) -> str:
    return value


def deserialize_json(data: str) -> NotificationSource:
    return cast(NotificationSource, data)
