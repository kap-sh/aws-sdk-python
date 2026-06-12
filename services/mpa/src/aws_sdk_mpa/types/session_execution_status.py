"""Generated from Smithy shape ``com.amazonaws.mpa#SessionExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

SessionExecutionStatus: TypeAlias = Literal[
    "EXECUTED",
    "FAILED",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXECUTED",
        "FAILED",
        "PENDING",
    )
)


def serialize_json(value: SessionExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionExecutionStatus value: {data!r}")
    return cast(SessionExecutionStatus, data)
