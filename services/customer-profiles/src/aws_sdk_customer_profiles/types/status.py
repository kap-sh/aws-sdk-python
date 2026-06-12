"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Status: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "SPLIT",
    "RETRY",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
        "SPLIT",
        "RETRY",
        "CANCELLED",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
