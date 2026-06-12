"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The current metric names.</p>"""
CurrentMetricName: TypeAlias = Literal[
    "AGENTS_ONLINE",
    "AGENTS_AVAILABLE",
    "AGENTS_ON_CALL",
    "AGENTS_NON_PRODUCTIVE",
    "AGENTS_AFTER_CONTACT_WORK",
    "AGENTS_ERROR",
    "AGENTS_STAFFED",
    "CONTACTS_IN_QUEUE",
    "OLDEST_CONTACT_AGE",
    "CONTACTS_SCHEDULED",
    "AGENTS_ON_CONTACT",
    "SLOTS_ACTIVE",
    "SLOTS_AVAILABLE",
    "ESTIMATED_WAIT_TIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGENTS_ONLINE",
        "AGENTS_AVAILABLE",
        "AGENTS_ON_CALL",
        "AGENTS_NON_PRODUCTIVE",
        "AGENTS_AFTER_CONTACT_WORK",
        "AGENTS_ERROR",
        "AGENTS_STAFFED",
        "CONTACTS_IN_QUEUE",
        "OLDEST_CONTACT_AGE",
        "CONTACTS_SCHEDULED",
        "AGENTS_ON_CONTACT",
        "SLOTS_ACTIVE",
        "SLOTS_AVAILABLE",
        "ESTIMATED_WAIT_TIME",
    )
)


def serialize_json(value: CurrentMetricName) -> str:
    return value


def deserialize_json(data: str) -> CurrentMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CurrentMetricName value: {data!r}")
    return cast(CurrentMetricName, data)
