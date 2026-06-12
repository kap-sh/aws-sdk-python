"""Generated from Smithy shape ``com.amazonaws.workdocs#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

SubscriptionType: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_json(value: SubscriptionType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionType value: {data!r}")
    return cast(SubscriptionType, data)
