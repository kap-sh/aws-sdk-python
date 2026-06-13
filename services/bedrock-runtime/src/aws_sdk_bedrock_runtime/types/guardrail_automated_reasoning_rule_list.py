"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule

GuardrailAutomatedReasoningRuleList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule.GuardrailAutomatedReasoningRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningRuleList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningRuleList:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule

    out: GuardrailAutomatedReasoningRuleList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule.deserialize_json(
                item
            )
        )
    return out
