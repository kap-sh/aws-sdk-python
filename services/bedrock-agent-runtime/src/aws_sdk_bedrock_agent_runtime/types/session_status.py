"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

SessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "ENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "EXPIRED",
        "ENDED",
    )
)


def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatus value: {data!r}")
    return cast(SessionStatus, data)
