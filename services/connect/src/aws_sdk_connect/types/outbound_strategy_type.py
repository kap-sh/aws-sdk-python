"""Generated from Smithy shape ``com.amazonaws.connect#OutboundStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

OutboundStrategyType: TypeAlias = Literal["AGENT_FIRST",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AGENT_FIRST",))


def serialize_json(value: OutboundStrategyType) -> str:
    return value


def deserialize_json(data: str) -> OutboundStrategyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutboundStrategyType value: {data!r}")
    return cast(OutboundStrategyType, data)
