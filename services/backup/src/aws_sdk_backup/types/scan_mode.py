"""Generated from Smithy shape ``com.amazonaws.backup#ScanMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

ScanMode: TypeAlias = Literal[
    "FULL_SCAN",
    "INCREMENTAL_SCAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_SCAN",
        "INCREMENTAL_SCAN",
    )
)


def serialize_json(value: ScanMode) -> str:
    return value


def deserialize_json(data: str) -> ScanMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanMode value: {data!r}")
    return cast(ScanMode, data)
