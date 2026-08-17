"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailManagedWordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_managed_word

GuardrailManagedWordList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_managed_word.GuardrailManagedWord"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordList) -> list:
    import capo_bedrock_runtime.types.guardrail_managed_word

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_managed_word.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailManagedWordList:
    import capo_bedrock_runtime.types.guardrail_managed_word

    out: GuardrailManagedWordList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_managed_word.deserialize_json(item)
        )
    return out
