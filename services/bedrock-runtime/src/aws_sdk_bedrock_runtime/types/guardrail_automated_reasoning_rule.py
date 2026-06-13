"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.automated_reasoning_rule_identifier
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_version_arn


class GuardrailAutomatedReasoningRule(TypedDict):
    identifier: NotRequired[
        "aws_sdk_bedrock_runtime.types.automated_reasoning_rule_identifier.AutomatedReasoningRuleIdentifier"
    ]
    """<p>The unique identifier of the automated reasoning rule.</p>"""
    policy_version_arn: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_policy_version_arn.GuardrailAutomatedReasoningPolicyVersionArn"
    ]
    """<p>The ARN of the automated reasoning policy version that contains this rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningRule) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "policy_version_arn" in value:
        out["policyVersionArn"] = value["policy_version_arn"]
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningRule:
    out: GuardrailAutomatedReasoningRule = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "policyVersionArn" in data:
        out["policy_version_arn"] = data["policyVersionArn"]
    return out
