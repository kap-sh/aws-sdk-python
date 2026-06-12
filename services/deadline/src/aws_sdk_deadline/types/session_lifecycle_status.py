"""Generated from Smithy shape ``com.amazonaws.deadline#SessionLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

SessionLifecycleStatus: TypeAlias = Literal[
    "STARTED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCEEDED",
    "UPDATE_FAILED",
    "ENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCEEDED",
        "UPDATE_FAILED",
        "ENDED",
    )
)


def serialize_json(value: SessionLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionLifecycleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionLifecycleStatus value: {data!r}")
    return cast(SessionLifecycleStatus, data)
