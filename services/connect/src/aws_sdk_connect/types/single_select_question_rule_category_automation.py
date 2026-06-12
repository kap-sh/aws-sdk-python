"""Generated from Smithy shape ``com.amazonaws.connect#SingleSelectQuestionRuleCategoryAutomation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_id
    import aws_sdk_connect.types.single_select_question_rule_category_automation_condition
    import aws_sdk_connect.types.single_select_question_rule_category_automation_label


class SingleSelectQuestionRuleCategoryAutomation(TypedDict):
    category: "aws_sdk_connect.types.single_select_question_rule_category_automation_label.SingleSelectQuestionRuleCategoryAutomationLabel"
    """<p> The category name, as defined in Rules.</p>"""
    condition: "aws_sdk_connect.types.single_select_question_rule_category_automation_condition.SingleSelectQuestionRuleCategoryAutomationCondition"
    """<p>The condition to apply for the automation option. If the condition is <code>PRESENT</code>, then the option is applied when the contact data includes the category. Similarly, if the condition is <code>NOT_PRESENT</code>, then the option is applied when the contact data does not include the category.</p>"""
    option_ref_id: "aws_sdk_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the answer option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleSelectQuestionRuleCategoryAutomation) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    import aws_sdk_connect.types.single_select_question_rule_category_automation_condition

    out["Condition"] = (
        aws_sdk_connect.types.single_select_question_rule_category_automation_condition.serialize_json(
            value["condition"]
        )
    )
    out["OptionRefId"] = value["option_ref_id"]
    return out


def deserialize_json(data: dict) -> SingleSelectQuestionRuleCategoryAutomation:
    out: SingleSelectQuestionRuleCategoryAutomation = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        out["category"] = data["Category"]
    else:
        raise DeserializationError(
            "SingleSelectQuestionRuleCategoryAutomation.category required"
        )
    if "Condition" in data:
        import aws_sdk_connect.types.single_select_question_rule_category_automation_condition

        out["condition"] = (
            aws_sdk_connect.types.single_select_question_rule_category_automation_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError(
            "SingleSelectQuestionRuleCategoryAutomation.condition required"
        )
    if "OptionRefId" in data:
        out["option_ref_id"] = data["OptionRefId"]
    else:
        raise DeserializationError(
            "SingleSelectQuestionRuleCategoryAutomation.option_ref_id required"
        )
    return out
