"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetricName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: CurrentMetricName) -> str:
    return value


def deserialize_json(data: str) -> CurrentMetricName:
    return cast(CurrentMetricName, data)
