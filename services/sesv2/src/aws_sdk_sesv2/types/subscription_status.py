"""Generated from Smithy shape ``com.amazonaws.sesv2#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

SubscriptionStatus: TypeAlias = Literal[
    "OPT_IN",
    "OPT_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPT_IN",
        "OPT_OUT",
    )
)


def serialize_json(value: SubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionStatus value: {data!r}")
    return cast(SubscriptionStatus, data)
