"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ScanStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "SKIPPED",
    )
)


def serialize_json(value: ScanStatus) -> str:
    return value


def deserialize_json(data: str) -> ScanStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanStatus value: {data!r}")
    return cast(ScanStatus, data)
