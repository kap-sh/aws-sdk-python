"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningStatement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_logic_content
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_natural_language_content


class GuardrailAutomatedReasoningStatement(TypedDict):
    logic: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_logic_content.GuardrailAutomatedReasoningStatementLogicContent"
    ]
    """<p>The formal logical representation of the statement.</p>"""
    natural_language: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_natural_language_content.GuardrailAutomatedReasoningStatementNaturalLanguageContent"
    ]
    """<p>The natural language explanation of the logical statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningStatement) -> dict:
    out: dict = {}
    if "logic" in value:
        out["logic"] = value["logic"]
    if "natural_language" in value:
        out["naturalLanguage"] = value["natural_language"]
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningStatement:
    out: GuardrailAutomatedReasoningStatement = {}  # type: ignore[typeddict-item]
    if "logic" in data:
        out["logic"] = data["logic"]
    if "naturalLanguage" in data:
        out["natural_language"] = data["naturalLanguage"]
    return out
