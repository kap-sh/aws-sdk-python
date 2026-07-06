"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningLogicWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning_type
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list


class GuardrailAutomatedReasoningLogicWarning(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning_type.GuardrailAutomatedReasoningLogicWarningType"
    ]
    """<p>The category of the detected logical issue, such as statements that are always true or always false.</p>"""
    premises: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.GuardrailAutomatedReasoningStatementList"
    ]
    """<p>The logical statements that serve as premises under which the claims are validated.</p>"""
    claims: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.GuardrailAutomatedReasoningStatementList"
    ]
    """<p>The logical statements that are validated while assuming the policy and premises.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningLogicWarning) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning_type

        out["type"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning_type.serialize_json(
                value["type"]
            )
        )
    if "premises" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["premises"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.serialize_json(
                value["premises"]
            )
        )
    if "claims" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["claims"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.serialize_json(
                value["claims"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningLogicWarning:
    out: GuardrailAutomatedReasoningLogicWarning = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning_type

        out["type"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning_type.deserialize_json(
                data["type"]
            )
        )
    if "premises" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["premises"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.deserialize_json(
                data["premises"]
            )
        )
    if "claims" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["claims"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.deserialize_json(
                data["claims"]
            )
        )
    return out
