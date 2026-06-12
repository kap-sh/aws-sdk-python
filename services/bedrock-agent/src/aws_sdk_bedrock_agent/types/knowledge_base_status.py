"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

KnowledgeBaseStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "UPDATING",
    "FAILED",
    "DELETE_UNSUCCESSFUL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "UPDATING",
        "FAILED",
        "DELETE_UNSUCCESSFUL",
    )
)


def serialize_json(value: KnowledgeBaseStatus) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KnowledgeBaseStatus value: {data!r}")
    return cast(KnowledgeBaseStatus, data)
