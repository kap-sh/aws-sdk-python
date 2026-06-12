"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ScanResult: TypeAlias = Literal[
    "CLEAN",
    "INFECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLEAN",
        "INFECTED",
    )
)


def serialize_json(value: ScanResult) -> str:
    return value


def deserialize_json(data: str) -> ScanResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanResult value: {data!r}")
    return cast(ScanResult, data)
