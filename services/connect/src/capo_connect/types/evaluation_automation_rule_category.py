"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAutomationRuleCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_transcript_points_of_interest
    import capo_connect.types.question_rule_category_automation_condition
    import capo_connect.types.question_rule_category_automation_label


class EvaluationAutomationRuleCategory(TypedDict, closed=True):
    category: "capo_connect.types.question_rule_category_automation_label.QuestionRuleCategoryAutomationLabel"
    """<p>A category label.</p>"""
    condition: "capo_connect.types.question_rule_category_automation_condition.QuestionRuleCategoryAutomationCondition"
    """<p>An automation condition for a Contact Lens category.</p>"""
    points_of_interest: NotRequired[
        "capo_connect.types.evaluation_transcript_points_of_interest.EvaluationTranscriptPointsOfInterest"
    ]
    """<p>A point of interest in a contact transcript that indicates match of condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAutomationRuleCategory) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    import capo_connect.types.question_rule_category_automation_condition

    out["Condition"] = (
        capo_connect.types.question_rule_category_automation_condition.serialize_json(
            value["condition"]
        )
    )
    if "points_of_interest" in value:
        import capo_connect.types.evaluation_transcript_points_of_interest

        out["PointsOfInterest"] = (
            capo_connect.types.evaluation_transcript_points_of_interest.serialize_json(
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
        import capo_connect.types.question_rule_category_automation_condition

        out["condition"] = (
            capo_connect.types.question_rule_category_automation_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationAutomationRuleCategory.condition required"
        )
    if "PointsOfInterest" in data:
        import capo_connect.types.evaluation_transcript_points_of_interest

        out["points_of_interest"] = (
            capo_connect.types.evaluation_transcript_points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    return out
