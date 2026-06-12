"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ScanType: TypeAlias = Literal[
    "GUARDDUTY_INITIATED",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GUARDDUTY_INITIATED",
        "ON_DEMAND",
    )
)


def serialize_json(value: ScanType) -> str:
    return value


def deserialize_json(data: str) -> ScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanType value: {data!r}")
    return cast(ScanType, data)
