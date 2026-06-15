"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Role``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

Role: TypeAlias = Literal[
    "ASSISTANT",
    "USER",
    "TOOL",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSISTANT",
        "USER",
        "TOOL",
        "OTHER",
    )
)


def serialize_json(value: Role) -> str:
    return value


def deserialize_json(data: str) -> Role:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Role value: {data!r}")
    return cast(Role, data)
