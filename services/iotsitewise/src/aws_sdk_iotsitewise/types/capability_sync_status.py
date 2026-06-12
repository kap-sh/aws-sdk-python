"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CapabilitySyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

CapabilitySyncStatus: TypeAlias = Literal[
    "IN_SYNC",
    "OUT_OF_SYNC",
    "SYNC_FAILED",
    "UNKNOWN",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_SYNC",
        "OUT_OF_SYNC",
        "SYNC_FAILED",
        "UNKNOWN",
        "NOT_APPLICABLE",
    )
)


def serialize_json(value: CapabilitySyncStatus) -> str:
    return value


def deserialize_json(data: str) -> CapabilitySyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilitySyncStatus value: {data!r}")
    return cast(CapabilitySyncStatus, data)
