"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

ContactStatus: TypeAlias = Literal[
    "SCHEDULING",
    "FAILED_TO_SCHEDULE",
    "SCHEDULED",
    "CANCELLED",
    "AWS_CANCELLED",
    "PREPASS",
    "PASS",
    "POSTPASS",
    "COMPLETED",
    "FAILED",
    "AVAILABLE",
    "CANCELLING",
    "AWS_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULING",
        "FAILED_TO_SCHEDULE",
        "SCHEDULED",
        "CANCELLED",
        "AWS_CANCELLED",
        "PREPASS",
        "PASS",
        "POSTPASS",
        "COMPLETED",
        "FAILED",
        "AVAILABLE",
        "CANCELLING",
        "AWS_FAILED",
    )
)


def serialize_json(value: ContactStatus) -> str:
    return value


def deserialize_json(data: str) -> ContactStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactStatus value: {data!r}")
    return cast(ContactStatus, data)
