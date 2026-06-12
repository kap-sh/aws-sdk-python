"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelAlertState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The possible states of a channel alert. SET - The alert is actively happening. CLEARED - The alert is no longer happening."""
ChannelAlertState: TypeAlias = Literal[
    "SET",
    "CLEARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SET",
        "CLEARED",
    )
)


def serialize_json(value: ChannelAlertState) -> str:
    return value


def deserialize_json(data: str) -> ChannelAlertState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelAlertState value: {data!r}")
    return cast(ChannelAlertState, data)
