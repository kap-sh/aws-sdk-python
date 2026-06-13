"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RoutingScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RoutingScope: TypeAlias = Literal[
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGIONAL",
        "GLOBAL",
    )
)


def serialize_json(value: RoutingScope) -> str:
    return value


def deserialize_json(data: str) -> RoutingScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingScope value: {data!r}")
    return cast(RoutingScope, data)
