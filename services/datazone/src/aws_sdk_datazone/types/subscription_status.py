"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

SubscriptionStatus: TypeAlias = Literal[
    "APPROVED",
    "REVOKED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "REVOKED",
        "CANCELLED",
    )
)


def serialize_json(value: SubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionStatus value: {data!r}")
    return cast(SubscriptionStatus, data)
