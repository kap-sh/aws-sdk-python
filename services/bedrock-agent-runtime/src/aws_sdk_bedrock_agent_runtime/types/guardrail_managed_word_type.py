"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailManagedWordType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailManagedWordType: TypeAlias = Literal["PROFANITY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PROFANITY",))


def serialize_json(value: GuardrailManagedWordType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailManagedWordType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailManagedWordType value: {data!r}")
    return cast(GuardrailManagedWordType, data)
