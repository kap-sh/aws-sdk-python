"""Generated from Smithy shape ``com.amazonaws.connect#AgentAvailabilityTimer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AgentAvailabilityTimer: TypeAlias = Literal[
    "TIME_SINCE_LAST_ACTIVITY",
    "TIME_SINCE_LAST_INBOUND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TIME_SINCE_LAST_ACTIVITY",
        "TIME_SINCE_LAST_INBOUND",
    )
)


def serialize_json(value: AgentAvailabilityTimer) -> str:
    return value


def deserialize_json(data: str) -> AgentAvailabilityTimer:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentAvailabilityTimer value: {data!r}")
    return cast(AgentAvailabilityTimer, data)
