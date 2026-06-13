"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

ScanJobState: TypeAlias = Literal[
    "COMPLETED",
    "COMPLETED_WITH_ISSUES",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "COMPLETED_WITH_ISSUES",
        "FAILED",
        "CANCELED",
    )
)


def serialize_json(value: ScanJobState) -> str:
    return value


def deserialize_json(data: str) -> ScanJobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanJobState value: {data!r}")
    return cast(ScanJobState, data)
