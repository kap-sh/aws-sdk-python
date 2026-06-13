"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list


class AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation(TypedDict):
    rule_ids: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.AutomatedReasoningPolicyDefinitionRuleIdList"
    ]
    """<p>The list of rule identifiers that the feedback applies to.</p>"""
    feedback: "aws_sdk_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language.AutomatedReasoningPolicyAnnotationFeedbackNaturalLanguage"
    """<p>The feedback information about rule performance, including suggestions for improvements or corrections.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation,
) -> dict:
    out: dict = {}
    if "rule_ids" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["ruleIds"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.serialize_json(
                value["rule_ids"]
            )
        )
    out["feedback"] = value["feedback"]
    return out


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation:
    out: AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation = {}  # type: ignore[typeddict-item]
    if "ruleIds" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["rule_ids"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.deserialize_json(
                data["ruleIds"]
            )
        )
    if "feedback" in data:
        out["feedback"] = data["feedback"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation.feedback required"
        )
    return out
