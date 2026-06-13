"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

CopyJobState: TypeAlias = Literal[
    "CREATED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "PARTIAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "PARTIAL",
    )
)


def serialize_json(value: CopyJobState) -> str:
    return value


def deserialize_json(data: str) -> CopyJobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CopyJobState value: {data!r}")
    return cast(CopyJobState, data)
