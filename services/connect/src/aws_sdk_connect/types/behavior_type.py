"""Generated from Smithy shape ``com.amazonaws.connect#BehaviorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

BehaviorType: TypeAlias = Literal[
    "ROUTE_CURRENT_CHANNEL_ONLY",
    "ROUTE_ANY_CHANNEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROUTE_CURRENT_CHANNEL_ONLY",
        "ROUTE_ANY_CHANNEL",
    )
)


def serialize_json(value: BehaviorType) -> str:
    return value


def deserialize_json(data: str) -> BehaviorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BehaviorType value: {data!r}")
    return cast(BehaviorType, data)
