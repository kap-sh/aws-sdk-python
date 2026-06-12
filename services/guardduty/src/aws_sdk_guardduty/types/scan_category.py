"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ScanCategory: TypeAlias = Literal[
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


def serialize_json(value: ScanCategory) -> str:
    return value


def deserialize_json(data: str) -> ScanCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanCategory value: {data!r}")
    return cast(ScanCategory, data)
