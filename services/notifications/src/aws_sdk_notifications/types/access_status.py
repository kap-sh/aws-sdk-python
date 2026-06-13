"""Generated from Smithy shape ``com.amazonaws.notifications#AccessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_notifications.errors import DeserializationError

AccessStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "PENDING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "PENDING",
        "FAILED",
    )
)


def serialize_json(value: AccessStatus) -> str:
    return value


def deserialize_json(data: str) -> AccessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessStatus value: {data!r}")
    return cast(AccessStatus, data)
