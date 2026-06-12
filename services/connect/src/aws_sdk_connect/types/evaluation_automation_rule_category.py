"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAutomationRuleCategory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_transcript_points_of_interest
    import aws_sdk_connect.types.question_rule_category_automation_condition
    import aws_sdk_connect.types.question_rule_category_automation_label


class EvaluationAutomationRuleCategory(TypedDict):
    category: "aws_sdk_connect.types.question_rule_category_automation_label.QuestionRuleCategoryAutomationLabel"
    """<p>A category label.</p>"""
    condition: "aws_sdk_connect.types.question_rule_category_automation_condition.QuestionRuleCategoryAutomationCondition"
    """<p>An automation condition for a Contact Lens category.</p>"""
    points_of_interest: NotRequired[
        "aws_sdk_connect.types.evaluation_transcript_points_of_interest.EvaluationTranscriptPointsOfInterest"
    ]
    """<p>A point of interest in a contact transcript that indicates match of condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAutomationRuleCategory) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    import aws_sdk_connect.types.question_rule_category_automation_condition

    out["Condition"] = (
        aws_sdk_connect.types.question_rule_category_automation_condition.serialize_json(
            value["condition"]
        )
    )
    if "points_of_interest" in value:
        import aws_sdk_connect.types.evaluation_transcript_points_of_interest

        out["PointsOfInterest"] = (
            aws_sdk_connect.types.evaluation_transcript_points_of_interest.serialize_json(
                value["points_of_interest"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationAutomationRuleCategory:
    out: EvaluationAutomationRuleCategory = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        out["category"] = data["Category"]
    else:
        raise DeserializationError("EvaluationAutomationRuleCategory.category required")
    if "Condition" in data:
        import aws_sdk_connect.types.question_rule_category_automation_condition

        out["condition"] = (
            aws_sdk_connect.types.question_rule_category_automation_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationAutomationRuleCategory.condition required"
        )
    if "PointsOfInterest" in data:
        import aws_sdk_connect.types.evaluation_transcript_points_of_interest

        out["points_of_interest"] = (
            aws_sdk_connect.types.evaluation_transcript_points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    return out
