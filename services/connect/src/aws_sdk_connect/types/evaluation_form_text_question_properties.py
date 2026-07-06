"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormTextQuestionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_text_question_automation


class EvaluationFormTextQuestionProperties(TypedDict, closed=True):
    automation: NotRequired[
        "aws_sdk_connect.types.evaluation_form_text_question_automation.EvaluationFormTextQuestionAutomation"
    ]
    """<p>The automation properties of the text question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormTextQuestionProperties) -> dict:
    out: dict = {}
    if "automation" in value:
        import aws_sdk_connect.types.evaluation_form_text_question_automation

        out["Automation"] = (
            aws_sdk_connect.types.evaluation_form_text_question_automation.serialize_json(
                value["automation"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormTextQuestionProperties:
    out: EvaluationFormTextQuestionProperties = {}  # type: ignore[typeddict-item]
    if "Automation" in data:
        import aws_sdk_connect.types.evaluation_form_text_question_automation

        out["automation"] = (
            aws_sdk_connect.types.evaluation_form_text_question_automation.deserialize_json(
                data["Automation"]
            )
        )
    return out
