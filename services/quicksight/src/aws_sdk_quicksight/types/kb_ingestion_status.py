"""Generated from Smithy shape ``com.amazonaws.quicksight#KbIngestionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

KbIngestionStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "FAILED",
    "COMPLETED",
    "INCOMPLETE",
    "CANCELLED",
    "CANCELLING",
    "TIMEOUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "RUNNING",
        "FAILED",
        "COMPLETED",
        "INCOMPLETE",
        "CANCELLED",
        "CANCELLING",
        "TIMEOUT",
    )
)


def serialize_json(value: KbIngestionStatus) -> str:
    return value


def deserialize_json(data: str) -> KbIngestionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KbIngestionStatus value: {data!r}")
    return cast(KbIngestionStatus, data)
