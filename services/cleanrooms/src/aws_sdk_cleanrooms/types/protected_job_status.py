"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ProtectedJobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "STARTED",
    "CANCELLED",
    "CANCELLING",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "STARTED",
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "SUCCESS",
    )
)


def serialize_json(value: ProtectedJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtectedJobStatus value: {data!r}")
    return cast(ProtectedJobStatus, data)
