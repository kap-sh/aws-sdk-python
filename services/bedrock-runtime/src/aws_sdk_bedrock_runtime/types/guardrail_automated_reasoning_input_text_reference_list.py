"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningInputTextReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference

GuardrailAutomatedReasoningInputTextReferenceList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference.GuardrailAutomatedReasoningInputTextReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningInputTextReferenceList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningInputTextReferenceList:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference

    out: GuardrailAutomatedReasoningInputTextReferenceList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference.deserialize_json(
                item
            )
        )
    return out
