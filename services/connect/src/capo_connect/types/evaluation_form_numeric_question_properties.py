"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormNumericQuestionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_numeric_question_automation
    import capo_connect.types.evaluation_form_numeric_question_option_list
    import capo_connect.types.integer


class EvaluationFormNumericQuestionProperties(TypedDict, closed=True):
    min_value: "capo_connect.types.integer.Integer"
    """<p>The minimum answer value.</p>"""
    max_value: "capo_connect.types.integer.Integer"
    """<p>The maximum answer value.</p>"""
    options: NotRequired[
        "capo_connect.types.evaluation_form_numeric_question_option_list.EvaluationFormNumericQuestionOptionList"
    ]
    """<p>The scoring options of the numeric question.</p>"""
    automation: NotRequired[
        "capo_connect.types.evaluation_form_numeric_question_automation.EvaluationFormNumericQuestionAutomation"
    ]
    """<p>The automation properties of the numeric question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormNumericQuestionProperties) -> dict:
    out: dict = {}
    out["MinValue"] = value.get("min_value", 0)
    out["MaxValue"] = value.get("max_value", 0)
    if "options" in value:
        import capo_connect.types.evaluation_form_numeric_question_option_list

        out["Options"] = (
            capo_connect.types.evaluation_form_numeric_question_option_list.serialize_json(
                value["options"]
            )
        )
    if "automation" in value:
        import capo_connect.types.evaluation_form_numeric_question_automation

        out["Automation"] = (
            capo_connect.types.evaluation_form_numeric_question_automation.serialize_json(
                value["automation"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormNumericQuestionProperties:
    out: EvaluationFormNumericQuestionProperties = {}  # type: ignore[typeddict-item]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    else:
        out["min_value"] = 0
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    else:
        out["max_value"] = 0
    if "Options" in data:
        import capo_connect.types.evaluation_form_numeric_question_option_list

        out["options"] = (
            capo_connect.types.evaluation_form_numeric_question_option_list.deserialize_json(
                data["Options"]
            )
        )
    if "Automation" in data:
        import capo_connect.types.evaluation_form_numeric_question_automation

        out["automation"] = (
            capo_connect.types.evaluation_form_numeric_question_automation.deserialize_json(
                data["Automation"]
            )
        )
    return out
