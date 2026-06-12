"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

RouteState: TypeAlias = Literal[
    "ACTIVE",
    "BLACKHOLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "BLACKHOLE",
    )
)


def serialize_json(value: RouteState) -> str:
    return value


def deserialize_json(data: str) -> RouteState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteState value: {data!r}")
    return cast(RouteState, data)
