"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailCustomWordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_custom_word

GuardrailCustomWordList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.guardrail_custom_word.GuardrailCustomWord"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCustomWordList) -> list:
    import capo_bedrock_agent_runtime.types.guardrail_custom_word

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_custom_word.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailCustomWordList:
    import capo_bedrock_agent_runtime.types.guardrail_custom_word

    out: GuardrailCustomWordList = []
    for item in data:
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_custom_word.deserialize_json(
                item
            )
        )
    return out
