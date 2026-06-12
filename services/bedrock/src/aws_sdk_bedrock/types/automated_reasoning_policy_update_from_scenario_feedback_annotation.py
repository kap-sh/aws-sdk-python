"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario_expression


class AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation(TypedDict):
    rule_ids: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.AutomatedReasoningPolicyDefinitionRuleIdList"
    ]
    """<p>The list of rule identifiers that were involved in the scenario being evaluated.</p>"""
    scenario_expression: "aws_sdk_bedrock.types.automated_reasoning_policy_scenario_expression.AutomatedReasoningPolicyScenarioExpression"
    """<p>The logical expression that defines the test scenario that generated this feedback.</p>"""
    feedback: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language.AutomatedReasoningPolicyAnnotationFeedbackNaturalLanguage"
    ]
    """<p>The feedback information about scenario performance, including any issues or improvements identified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation,
) -> dict:
    out: dict = {}
    if "rule_ids" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["ruleIds"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.serialize_json(
                value["rule_ids"]
            )
        )
    out["scenarioExpression"] = value["scenario_expression"]
    if "feedback" in value:
        out["feedback"] = value["feedback"]
    return out


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation:
    out: AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation = {}  # type: ignore[typeddict-item]
    if "ruleIds" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["rule_ids"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.deserialize_json(
                data["ruleIds"]
            )
        )
    if "scenarioExpression" in data:
        out["scenario_expression"] = data["scenarioExpression"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation.scenario_expression required"
        )
    if "feedback" in data:
        out["feedback"] = data["feedback"]
    return out
