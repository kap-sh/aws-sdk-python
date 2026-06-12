"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddRuleMutation``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule


class AutomatedReasoningPolicyAddRuleMutation(TypedDict):
    rule: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"
    """<p>The rule definition that specifies the formal logical expression and metadata for the new rule being added to the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddRuleMutation) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

    out["rule"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
            value["rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddRuleMutation:
    out: AutomatedReasoningPolicyAddRuleMutation = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

        out["rule"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                data["rule"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddRuleMutation.rule required"
        )
    return out
