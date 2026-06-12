"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AgentStatusState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AgentStatusState) -> str:
    return value


def deserialize_json(data: str) -> AgentStatusState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatusState value: {data!r}")
    return cast(AgentStatusState, data)
