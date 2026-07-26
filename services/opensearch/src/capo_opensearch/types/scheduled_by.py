"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledBy``."""

from typing import Literal, TypeAlias, cast

ScheduledBy: TypeAlias = Literal[
    "CUSTOMER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledBy) -> str:
    return value


def deserialize_json(data: str) -> ScheduledBy:
    return cast(ScheduledBy, data)
