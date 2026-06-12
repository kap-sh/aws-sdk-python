"""Generated from Smithy shape ``com.amazonaws.outposts#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

SubscriptionStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "INACTIVE",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING",
        "INACTIVE",
        "CANCELLED",
    )
)


def serialize_json(value: SubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionStatus value: {data!r}")
    return cast(SubscriptionStatus, data)
