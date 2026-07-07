"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationContactLensAnswerAnalysisDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_automation_rule_category_list


class EvaluationContactLensAnswerAnalysisDetails(TypedDict, closed=True):
    matched_rule_categories: NotRequired[
        "aws_sdk_connect.types.evaluation_automation_rule_category_list.EvaluationAutomationRuleCategoryList"
    ]
    """<p>A list of match rule categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationContactLensAnswerAnalysisDetails) -> dict:
    out: dict = {}
    if "matched_rule_categories" in value:
        import aws_sdk_connect.types.evaluation_automation_rule_category_list

        out["MatchedRuleCategories"] = (
            aws_sdk_connect.types.evaluation_automation_rule_category_list.serialize_json(
                value["matched_rule_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationContactLensAnswerAnalysisDetails:
    out: EvaluationContactLensAnswerAnalysisDetails = {}  # type: ignore[typeddict-item]
    if "MatchedRuleCategories" in data:
        import aws_sdk_connect.types.evaluation_automation_rule_category_list

        out["matched_rule_categories"] = (
            aws_sdk_connect.types.evaluation_automation_rule_category_list.deserialize_json(
                data["MatchedRuleCategories"]
            )
        )
    return out
