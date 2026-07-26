"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_single_select_question_automation
    import capo_connect.types.evaluation_form_single_select_question_display_mode
    import capo_connect.types.evaluation_form_single_select_question_option_list


class EvaluationFormSingleSelectQuestionProperties(TypedDict, closed=True):
    options: "capo_connect.types.evaluation_form_single_select_question_option_list.EvaluationFormSingleSelectQuestionOptionList"
    """<p>The answer options of the single select question.</p>"""
    display_as: NotRequired[
        "capo_connect.types.evaluation_form_single_select_question_display_mode.EvaluationFormSingleSelectQuestionDisplayMode"
    ]
    """<p>The display mode of the single select question.</p>"""
    automation: NotRequired[
        "capo_connect.types.evaluation_form_single_select_question_automation.EvaluationFormSingleSelectQuestionAutomation"
    ]
    """<p>The display mode of the single select question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionProperties) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_single_select_question_option_list

    out["Options"] = (
        capo_connect.types.evaluation_form_single_select_question_option_list.serialize_json(
            value["options"]
        )
    )
    if "display_as" in value:
        import capo_connect.types.evaluation_form_single_select_question_display_mode

        out["DisplayAs"] = (
            capo_connect.types.evaluation_form_single_select_question_display_mode.serialize_json(
                value["display_as"]
            )
        )
    if "automation" in value:
        import capo_connect.types.evaluation_form_single_select_question_automation

        out["Automation"] = (
            capo_connect.types.evaluation_form_single_select_question_automation.serialize_json(
                value["automation"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormSingleSelectQuestionProperties:
    out: EvaluationFormSingleSelectQuestionProperties = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_connect.types.evaluation_form_single_select_question_option_list

        out["options"] = (
            capo_connect.types.evaluation_form_single_select_question_option_list.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormSingleSelectQuestionProperties.options required"
        )
    if "DisplayAs" in data:
        import capo_connect.types.evaluation_form_single_select_question_display_mode

        out["display_as"] = (
            capo_connect.types.evaluation_form_single_select_question_display_mode.deserialize_json(
                data["DisplayAs"]
            )
        )
    if "Automation" in data:
        import capo_connect.types.evaluation_form_single_select_question_automation

        out["automation"] = (
            capo_connect.types.evaluation_form_single_select_question_automation.deserialize_json(
                data["Automation"]
            )
        )
    return out
