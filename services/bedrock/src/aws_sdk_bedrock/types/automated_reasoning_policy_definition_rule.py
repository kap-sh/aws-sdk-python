"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_alternate_expression
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_expression
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id


class AutomatedReasoningPolicyDefinitionRule(TypedDict):
    id: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    """<p>The unique identifier of the rule within the policy.</p>"""
    expression: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_expression.AutomatedReasoningPolicyDefinitionRuleExpression"
    """<p>The formal logic expression of the rule.</p>"""
    alternate_expression: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_alternate_expression.AutomatedReasoningPolicyDefinitionRuleAlternateExpression"
    ]
    """<p>The human-readable form of the rule expression, often in natural language or simplified notation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionRule) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["expression"] = value["expression"]
    if "alternate_expression" in value:
        out["alternateExpression"] = value["alternate_expression"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionRule:
    out: AutomatedReasoningPolicyDefinitionRule = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AutomatedReasoningPolicyDefinitionRule.id required")
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionRule.expression required"
        )
    if "alternateExpression" in data:
        out["alternate_expression"] = data["alternateExpression"]
    return out
