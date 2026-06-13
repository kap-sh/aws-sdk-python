"""Generated from Smithy shape ``com.amazonaws.backup#ScanState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

ScanState: TypeAlias = Literal[
    "CANCELED",
    "COMPLETED",
    "COMPLETED_WITH_ISSUES",
    "CREATED",
    "FAILED",
    "RUNNING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANCELED",
        "COMPLETED",
        "COMPLETED_WITH_ISSUES",
        "CREATED",
        "FAILED",
        "RUNNING",
    )
)


def serialize_json(value: ScanState) -> str:
    return value


def deserialize_json(data: str) -> ScanState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanState value: {data!r}")
    return cast(ScanState, data)
