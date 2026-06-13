"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement

GuardrailAutomatedReasoningStatementList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement.GuardrailAutomatedReasoningStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningStatementList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningStatementList:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement

    out: GuardrailAutomatedReasoningStatementList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement.deserialize_json(
                item
            )
        )
    return out
