"""Generated from Smithy shape ``com.amazonaws.iotwireless#ImportTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

ImportTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "INITIALIZED",
    "PENDING",
    "COMPLETE",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZING",
        "INITIALIZED",
        "PENDING",
        "COMPLETE",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: ImportTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportTaskStatus value: {data!r}")
    return cast(ImportTaskStatus, data)
