"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailWordPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailWordPolicyAction: TypeAlias = Literal["BLOCKED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BLOCKED",))


def serialize_json(value: GuardrailWordPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailWordPolicyAction value: {data!r}")
    return cast(GuardrailWordPolicyAction, data)
