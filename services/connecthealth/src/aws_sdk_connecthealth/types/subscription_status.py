"""Generated from Smithy shape ``com.amazonaws.connecthealth#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

SubscriptionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "DELETED",
    )
)


def serialize_json(value: SubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionStatus value: {data!r}")
    return cast(SubscriptionStatus, data)
