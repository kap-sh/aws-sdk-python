"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

Protocol: TypeAlias = Literal["WebRTC",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WebRTC",))


def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
