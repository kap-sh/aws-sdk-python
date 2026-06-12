"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddRuleAnnotation``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_expression


class AutomatedReasoningPolicyAddRuleAnnotation(TypedDict):
    expression: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_expression.AutomatedReasoningPolicyDefinitionRuleExpression"
    """<p>The formal logical expression that defines the rule, using mathematical notation and referencing policy variables and types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddRuleAnnotation) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddRuleAnnotation:
    out: AutomatedReasoningPolicyAddRuleAnnotation = {}  # type: ignore[typeddict-item]
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddRuleAnnotation.expression required"
        )
    return out
