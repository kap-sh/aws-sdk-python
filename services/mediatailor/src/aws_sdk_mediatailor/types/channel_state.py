"""Generated from Smithy shape ``com.amazonaws.mediatailor#ChannelState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

ChannelState: TypeAlias = Literal[
    "RUNNING",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "STOPPED",
    )
)


def serialize_json(value: ChannelState) -> str:
    return value


def deserialize_json(data: str) -> ChannelState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelState value: {data!r}")
    return cast(ChannelState, data)
