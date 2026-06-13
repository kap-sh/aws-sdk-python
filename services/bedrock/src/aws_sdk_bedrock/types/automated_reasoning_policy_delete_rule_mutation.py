"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteRuleMutation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id


class AutomatedReasoningPolicyDeleteRuleMutation(TypedDict):
    id: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    """<p>The unique identifier of the rule to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteRuleMutation) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteRuleMutation:
    out: AutomatedReasoningPolicyDeleteRuleMutation = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDeleteRuleMutation.id required"
        )
    return out
