"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailContentPolicyAction: TypeAlias = Literal["BLOCKED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BLOCKED",))


def serialize_json(value: GuardrailContentPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContentPolicyAction value: {data!r}"
        )
    return cast(GuardrailContentPolicyAction, data)
