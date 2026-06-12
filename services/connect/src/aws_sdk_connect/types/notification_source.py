"""Generated from Smithy shape ``com.amazonaws.connect#NotificationSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The source that created the notification. Possible values include CUSTOMER (user-created), RULES (rule-generated), and SYSTEM (system-generated).</p>"""
NotificationSource: TypeAlias = Literal[
    "CUSTOMER",
    "RULES",
    "SYSTEM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER",
        "RULES",
        "SYSTEM",
    )
)


def serialize_json(value: NotificationSource) -> str:
    return value


def deserialize_json(data: str) -> NotificationSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationSource value: {data!r}")
    return cast(NotificationSource, data)
