"""Generated from Smithy shape ``com.amazonaws.groundstation#AgentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

AgentStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILED",
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: AgentStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatus value: {data!r}")
    return cast(AgentStatus, data)
