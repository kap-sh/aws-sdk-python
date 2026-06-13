"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextToSqlConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

TextToSqlConfigurationType: TypeAlias = Literal["KNOWLEDGE_BASE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KNOWLEDGE_BASE",))


def serialize_json(value: TextToSqlConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> TextToSqlConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TextToSqlConfigurationType value: {data!r}"
        )
    return cast(TextToSqlConfigurationType, data)
