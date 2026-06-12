"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

KnowledgeBaseType: TypeAlias = Literal[
    "VECTOR",
    "KENDRA",
    "SQL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VECTOR",
        "KENDRA",
        "SQL",
    )
)


def serialize_json(value: KnowledgeBaseType) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KnowledgeBaseType value: {data!r}")
    return cast(KnowledgeBaseType, data)
