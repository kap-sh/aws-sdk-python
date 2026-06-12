"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptTemplateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

PromptTemplateType: TypeAlias = Literal[
    "TEXT",
    "CHAT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "CHAT",
    )
)


def serialize_json(value: PromptTemplateType) -> str:
    return value


def deserialize_json(data: str) -> PromptTemplateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptTemplateType value: {data!r}")
    return cast(PromptTemplateType, data)
