"""Generated from Smithy shape ``com.amazonaws.mpa#SessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

SessionStatus: TypeAlias = Literal[
    "PENDING",
    "CANCELLED",
    "APPROVED",
    "FAILED",
    "CREATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CANCELLED",
        "APPROVED",
        "FAILED",
        "CREATING",
    )
)


def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatus value: {data!r}")
    return cast(SessionStatus, data)
