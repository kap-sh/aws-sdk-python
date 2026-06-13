"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningTranslationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_option

GuardrailAutomatedReasoningTranslationOptionList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_option.GuardrailAutomatedReasoningTranslationOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningTranslationOptionList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningTranslationOptionList:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_option

    out: GuardrailAutomatedReasoningTranslationOptionList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_option.deserialize_json(
                item
            )
        )
    return out
