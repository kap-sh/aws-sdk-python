"""Generated from Smithy shape ``com.amazonaws.outposts#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

SubscriptionType: TypeAlias = Literal[
    "ORIGINAL",
    "RENEWAL",
    "CAPACITY_INCREASE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORIGINAL",
        "RENEWAL",
        "CAPACITY_INCREASE",
    )
)


def serialize_json(value: SubscriptionType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionType value: {data!r}")
    return cast(SubscriptionType, data)
