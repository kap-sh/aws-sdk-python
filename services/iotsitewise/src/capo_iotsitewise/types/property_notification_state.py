"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyNotificationState``."""

from typing import Literal, TypeAlias, cast

PropertyNotificationState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyNotificationState) -> str:
    return value


def deserialize_json(data: str) -> PropertyNotificationState:
    return cast(PropertyNotificationState, data)
