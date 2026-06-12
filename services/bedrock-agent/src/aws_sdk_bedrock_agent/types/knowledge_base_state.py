"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

KnowledgeBaseState: TypeAlias = Literal[
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


def serialize_json(value: KnowledgeBaseState) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KnowledgeBaseState value: {data!r}")
    return cast(KnowledgeBaseState, data)
