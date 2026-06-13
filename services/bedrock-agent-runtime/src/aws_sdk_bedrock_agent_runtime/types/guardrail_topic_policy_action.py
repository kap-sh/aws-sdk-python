"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailTopicPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailTopicPolicyAction: TypeAlias = Literal["BLOCKED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BLOCKED",))


def serialize_json(value: GuardrailTopicPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailTopicPolicyAction value: {data!r}"
        )
    return cast(GuardrailTopicPolicyAction, data)
