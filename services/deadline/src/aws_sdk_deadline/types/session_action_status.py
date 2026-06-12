"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

SessionActionStatus: TypeAlias = Literal[
    "ASSIGNED",
    "RUNNING",
    "CANCELING",
    "SUCCEEDED",
    "FAILED",
    "INTERRUPTED",
    "CANCELED",
    "NEVER_ATTEMPTED",
    "SCHEDULED",
    "RECLAIMING",
    "RECLAIMED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSIGNED",
        "RUNNING",
        "CANCELING",
        "SUCCEEDED",
        "FAILED",
        "INTERRUPTED",
        "CANCELED",
        "NEVER_ATTEMPTED",
        "SCHEDULED",
        "RECLAIMING",
        "RECLAIMED",
    )
)


def serialize_json(value: SessionActionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionActionStatus value: {data!r}")
    return cast(SessionActionStatus, data)
