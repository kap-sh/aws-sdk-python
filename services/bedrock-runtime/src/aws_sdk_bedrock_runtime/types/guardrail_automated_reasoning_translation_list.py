"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningTranslationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation

GuardrailAutomatedReasoningTranslationList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.GuardrailAutomatedReasoningTranslation"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningTranslationList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningTranslationList:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation

    out: GuardrailAutomatedReasoningTranslationList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.deserialize_json(
                item
            )
        )
    return out
