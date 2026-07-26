"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormNumericQuestionOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.automatic_fail_configuration
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_form_question_answer_score
    import capo_connect.types.integer


class EvaluationFormNumericQuestionOption(TypedDict, closed=True):
    min_value: "capo_connect.types.integer.Integer"
    """<p>The minimum answer value of the range option.</p>"""
    max_value: "capo_connect.types.integer.Integer"
    """<p>The maximum answer value of the range option.</p>"""
    score: "capo_connect.types.evaluation_form_question_answer_score.EvaluationFormQuestionAnswerScore"
    """<p>The score assigned to answer values within the range option.</p>"""
    automatic_fail: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.</p>"""
    automatic_fail_configuration: NotRequired[
        "capo_connect.types.automatic_fail_configuration.AutomaticFailConfiguration"
    ]
    """<p>A configuration for automatic fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormNumericQuestionOption) -> dict:
    out: dict = {}
    out["MinValue"] = value.get("min_value", 0)
    out["MaxValue"] = value.get("max_value", 0)
    out["Score"] = value.get("score", 0)
    out["AutomaticFail"] = value.get("automatic_fail", False)
    if "automatic_fail_configuration" in value:
        import capo_connect.types.automatic_fail_configuration

        out["AutomaticFailConfiguration"] = (
            capo_connect.types.automatic_fail_configuration.serialize_json(
                value["automatic_fail_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormNumericQuestionOption:
    out: EvaluationFormNumericQuestionOption = {}  # type: ignore[typeddict-item]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    else:
        out["min_value"] = 0
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    else:
        out["max_value"] = 0
    if "Score" in data:
        out["score"] = data["Score"]
    else:
        out["score"] = 0
    if "AutomaticFail" in data:
        out["automatic_fail"] = data["AutomaticFail"]
    else:
        out["automatic_fail"] = False
    if "AutomaticFailConfiguration" in data:
        import capo_connect.types.automatic_fail_configuration

        out["automatic_fail_configuration"] = (
            capo_connect.types.automatic_fail_configuration.deserialize_json(
                data["AutomaticFailConfiguration"]
            )
        )
    return out
