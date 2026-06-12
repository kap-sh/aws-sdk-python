"""Generated from Smithy shape ``com.amazonaws.connect#MultiSelectQuestionRuleCategoryAutomation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.multi_select_question_rule_category_automation_condition
    import aws_sdk_connect.types.multi_select_question_rule_category_automation_label
    import aws_sdk_connect.types.reference_id_list


class MultiSelectQuestionRuleCategoryAutomation(TypedDict):
    category: "aws_sdk_connect.types.multi_select_question_rule_category_automation_label.MultiSelectQuestionRuleCategoryAutomationLabel"
    """<p>The category name for this automation rule.</p>"""
    condition: "aws_sdk_connect.types.multi_select_question_rule_category_automation_condition.MultiSelectQuestionRuleCategoryAutomationCondition"
    """<p>The condition for this automation rule.</p>"""
    option_ref_ids: "aws_sdk_connect.types.reference_id_list.ReferenceIdList"
    """<p>Reference IDs of options for this automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiSelectQuestionRuleCategoryAutomation) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    import aws_sdk_connect.types.multi_select_question_rule_category_automation_condition

    out["Condition"] = (
        aws_sdk_connect.types.multi_select_question_rule_category_automation_condition.serialize_json(
            value["condition"]
        )
    )
    import aws_sdk_connect.types.reference_id_list

    out["OptionRefIds"] = aws_sdk_connect.types.reference_id_list.serialize_json(
        value["option_ref_ids"]
    )
    return out


def deserialize_json(data: dict) -> MultiSelectQuestionRuleCategoryAutomation:
    out: MultiSelectQuestionRuleCategoryAutomation = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        out["category"] = data["Category"]
    else:
        raise DeserializationError(
            "MultiSelectQuestionRuleCategoryAutomation.category required"
        )
    if "Condition" in data:
        import aws_sdk_connect.types.multi_select_question_rule_category_automation_condition

        out["condition"] = (
            aws_sdk_connect.types.multi_select_question_rule_category_automation_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError(
            "MultiSelectQuestionRuleCategoryAutomation.condition required"
        )
    if "OptionRefIds" in data:
        import aws_sdk_connect.types.reference_id_list

        out["option_ref_ids"] = (
            aws_sdk_connect.types.reference_id_list.deserialize_json(
                data["OptionRefIds"]
            )
        )
    else:
        raise DeserializationError(
            "MultiSelectQuestionRuleCategoryAutomation.option_ref_ids required"
        )
    return out
