"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

SessionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatus value: {data!r}")
    return cast(SessionStatus, data)
