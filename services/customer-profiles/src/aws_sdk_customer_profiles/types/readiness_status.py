"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ReadinessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

ReadinessStatus: TypeAlias = Literal[
    "PREPARING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREPARING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: ReadinessStatus) -> str:
    return value


def deserialize_json(data: str) -> ReadinessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReadinessStatus value: {data!r}")
    return cast(ReadinessStatus, data)
