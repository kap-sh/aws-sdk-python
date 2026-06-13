"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseQueryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

KnowledgeBaseQueryType: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "IMAGE",
    )
)


def serialize_json(value: KnowledgeBaseQueryType) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseQueryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KnowledgeBaseQueryType value: {data!r}")
    return cast(KnowledgeBaseQueryType, data)
