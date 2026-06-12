"""Generated from Smithy shape ``com.amazonaws.xray#RetrievalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

RetrievalStatus: TypeAlias = Literal[
    "SCHEDULED",
    "RUNNING",
    "COMPLETE",
    "FAILED",
    "CANCELLED",
    "TIMEOUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "RUNNING",
        "COMPLETE",
        "FAILED",
        "CANCELLED",
        "TIMEOUT",
    )
)


def serialize_json(value: RetrievalStatus) -> str:
    return value


def deserialize_json(data: str) -> RetrievalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetrievalStatus value: {data!r}")
    return cast(RetrievalStatus, data)
