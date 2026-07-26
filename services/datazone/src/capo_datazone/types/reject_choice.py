"""Generated from Smithy shape ``com.amazonaws.datazone#RejectChoice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.prediction_choices


class RejectChoice(TypedDict, closed=True):
    prediction_target: NotRequired["str"]
    """<p>Specifies the target (for example, a column name) where a prediction can be rejected.</p>"""
    prediction_choices: NotRequired[
        "capo_datazone.types.prediction_choices.PredictionChoices"
    ]
    """<p>Specifies the the automatically generated business metadata that can be rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectChoice) -> dict:
    out: dict = {}
    if "prediction_target" in value:
        out["predictionTarget"] = value["prediction_target"]
    if "prediction_choices" in value:
        import capo_datazone.types.prediction_choices

        out["predictionChoices"] = (
            capo_datazone.types.prediction_choices.serialize_json(
                value["prediction_choices"]
            )
        )
    return out


def deserialize_json(data: dict) -> RejectChoice:
    out: RejectChoice = {}  # type: ignore[typeddict-item]
    if "predictionTarget" in data:
        out["prediction_target"] = data["predictionTarget"]
    if "predictionChoices" in data:
        import capo_datazone.types.prediction_choices

        out["prediction_choices"] = (
            capo_datazone.types.prediction_choices.deserialize_json(
                data["predictionChoices"]
            )
        )
    return out
