"""Generated from Smithy shape ``com.amazonaws.backup#ScanResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

ScanResultStatus: TypeAlias = Literal[
    "NO_THREATS_FOUND",
    "THREATS_FOUND",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_THREATS_FOUND",
        "THREATS_FOUND",
        "UNKNOWN",
    )
)


def serialize_json(value: ScanResultStatus) -> str:
    return value


def deserialize_json(data: str) -> ScanResultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanResultStatus value: {data!r}")
    return cast(ScanResultStatus, data)
