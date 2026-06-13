"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

InvocationType: TypeAlias = Literal[
    "ACTION_GROUP",
    "KNOWLEDGE_BASE",
    "FINISH",
    "ACTION_GROUP_CODE_INTERPRETER",
    "AGENT_COLLABORATOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTION_GROUP",
        "KNOWLEDGE_BASE",
        "FINISH",
        "ACTION_GROUP_CODE_INTERPRETER",
        "AGENT_COLLABORATOR",
    )
)


def serialize_json(value: InvocationType) -> str:
    return value


def deserialize_json(data: str) -> InvocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvocationType value: {data!r}")
    return cast(InvocationType, data)
