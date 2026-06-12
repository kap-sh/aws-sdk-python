"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyNotificationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

PropertyNotificationState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: PropertyNotificationState) -> str:
    return value


def deserialize_json(data: str) -> PropertyNotificationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyNotificationState value: {data!r}")
    return cast(PropertyNotificationState, data)
