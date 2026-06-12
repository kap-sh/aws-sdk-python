"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateRuleMutation``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule


class AutomatedReasoningPolicyUpdateRuleMutation(TypedDict):
    rule: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"
    """<p>The updated rule definition containing the modified formal logical expression and any changed metadata for the existing rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateRuleMutation) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

    out["rule"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
            value["rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateRuleMutation:
    out: AutomatedReasoningPolicyUpdateRuleMutation = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

        out["rule"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                data["rule"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateRuleMutation.rule required"
        )
    return out
