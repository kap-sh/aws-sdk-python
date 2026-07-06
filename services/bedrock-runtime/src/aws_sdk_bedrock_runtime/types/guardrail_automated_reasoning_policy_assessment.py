"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding_list


class GuardrailAutomatedReasoningPolicyAssessment(TypedDict, closed=True):
    findings: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding_list.GuardrailAutomatedReasoningFindingList"
    ]
    """<p>List of logical validation results produced by evaluating the input content against automated reasoning policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningPolicyAssessment) -> dict:
    out: dict = {}
    if "findings" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding_list

        out["findings"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding_list.serialize_json(
                value["findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningPolicyAssessment:
    out: GuardrailAutomatedReasoningPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding_list

        out["findings"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding_list.deserialize_json(
                data["findings"]
            )
        )
    return out
