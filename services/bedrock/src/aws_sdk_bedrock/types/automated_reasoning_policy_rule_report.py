"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyRuleReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_accuracy_score
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_justification_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_justification_text
    import aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference_list


class AutomatedReasoningPolicyRuleReport(TypedDict, closed=True):
    rule: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    """<p>The identifier of the policy rule being analyzed in this report.</p>"""
    grounding_statements: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference_list.AutomatedReasoningPolicyStatementReferenceList"
    ]
    """<p>References to statements from the source documents that provide the basis or justification for this rule.</p>"""
    grounding_justifications: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_justification_list.AutomatedReasoningPolicyJustificationList"
    ]
    """<p>Explanations describing how the source statements support and justify this specific rule.</p>"""
    accuracy_score: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_accuracy_score.AutomatedReasoningPolicyAccuracyScore"
    ]
    """<p>A score from 0.0 to 1.0 indicating how accurately this rule represents the source material.</p>"""
    accuracy_justification: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_justification_text.AutomatedReasoningPolicyJustificationText"
    ]
    """<p>A textual explanation of the accuracy score, describing why the rule received this particular accuracy rating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyRuleReport) -> dict:
    out: dict = {}
    out["rule"] = value["rule"]
    if "grounding_statements" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference_list

        out["groundingStatements"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference_list.serialize_json(
                value["grounding_statements"]
            )
        )
    if "grounding_justifications" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_justification_list

        out["groundingJustifications"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_justification_list.serialize_json(
                value["grounding_justifications"]
            )
        )
    if "accuracy_score" in value:
        out["accuracyScore"] = value["accuracy_score"]
    if "accuracy_justification" in value:
        out["accuracyJustification"] = value["accuracy_justification"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyRuleReport:
    out: AutomatedReasoningPolicyRuleReport = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        out["rule"] = data["rule"]
    else:
        raise DeserializationError("AutomatedReasoningPolicyRuleReport.rule required")
    if "groundingStatements" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference_list

        out["grounding_statements"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference_list.deserialize_json(
                data["groundingStatements"]
            )
        )
    if "groundingJustifications" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_justification_list

        out["grounding_justifications"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_justification_list.deserialize_json(
                data["groundingJustifications"]
            )
        )
    if "accuracyScore" in data:
        out["accuracy_score"] = data["accuracyScore"]
    if "accuracyJustification" in data:
        out["accuracy_justification"] = data["accuracyJustification"]
    return out
