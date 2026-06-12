"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AgentStatusType: TypeAlias = Literal[
    "ROUTABLE",
    "CUSTOM",
    "OFFLINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROUTABLE",
        "CUSTOM",
        "OFFLINE",
    )
)


def serialize_json(value: AgentStatusType) -> str:
    return value


def deserialize_json(data: str) -> AgentStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatusType value: {data!r}")
    return cast(AgentStatusType, data)
