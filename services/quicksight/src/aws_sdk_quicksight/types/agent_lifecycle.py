"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AgentLifecycle: TypeAlias = Literal[
    "PREVIEW",
    "PUBLISHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREVIEW",
        "PUBLISHED",
    )
)


def serialize_json(value: AgentLifecycle) -> str:
    return value


def deserialize_json(data: str) -> AgentLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentLifecycle value: {data!r}")
    return cast(AgentLifecycle, data)
