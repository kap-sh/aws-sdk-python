"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

IngestionStatus: TypeAlias = Literal[
    "INITIALIZED",
    "QUEUED",
    "RUNNING",
    "FAILED",
    "COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "QUEUED",
        "RUNNING",
        "FAILED",
        "COMPLETED",
        "CANCELLED",
    )
)


def serialize_json(value: IngestionStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionStatus value: {data!r}")
    return cast(IngestionStatus, data)
