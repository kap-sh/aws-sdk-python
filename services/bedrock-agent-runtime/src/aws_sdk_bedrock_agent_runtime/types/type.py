"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

Type: TypeAlias = Literal[
    "ACTION_GROUP",
    "AGENT_COLLABORATOR",
    "KNOWLEDGE_BASE",
    "FINISH",
    "ASK_USER",
    "REPROMPT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTION_GROUP",
        "AGENT_COLLABORATOR",
        "KNOWLEDGE_BASE",
        "FINISH",
        "ASK_USER",
        "REPROMPT",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
