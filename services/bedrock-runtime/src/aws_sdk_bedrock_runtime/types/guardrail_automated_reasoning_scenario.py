"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningScenario``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list


class GuardrailAutomatedReasoningScenario(TypedDict):
    statements: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.GuardrailAutomatedReasoningStatementList"
    ]
    """<p>List of logical assignments and statements that define this scenario.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningScenario) -> dict:
    out: dict = {}
    if "statements" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["statements"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.serialize_json(
                value["statements"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningScenario:
    out: GuardrailAutomatedReasoningScenario = {}  # type: ignore[typeddict-item]
    if "statements" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["statements"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.deserialize_json(
                data["statements"]
            )
        )
    return out
