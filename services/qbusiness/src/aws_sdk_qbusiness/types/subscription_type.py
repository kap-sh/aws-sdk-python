"""Generated from Smithy shape ``com.amazonaws.qbusiness#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

SubscriptionType: TypeAlias = Literal[
    "Q_LITE",
    "Q_BUSINESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Q_LITE",
        "Q_BUSINESS",
    )
)


def serialize_json(value: SubscriptionType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionType value: {data!r}")
    return cast(SubscriptionType, data)
