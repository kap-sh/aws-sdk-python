"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AgentStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
    "FAILED",
    "CREATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UPDATING",
        "FAILED",
        "CREATING",
    )
)


def serialize_json(value: AgentStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatus value: {data!r}")
    return cast(AgentStatus, data)
