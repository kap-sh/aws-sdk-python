"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelVersionEvaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.prediction_explanations
    import capo_frauddetector.types.string


class ModelVersionEvaluation(TypedDict, closed=True):
    output_variable_name: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The output variable name. </p>"""
    evaluation_score: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The evaluation score generated for the model version. </p>"""
    prediction_explanations: NotRequired[
        "capo_frauddetector.types.prediction_explanations.PredictionExplanations"
    ]
    """<p> The prediction explanations generated for the model version. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVersionEvaluation) -> dict:
    out: dict = {}
    if "output_variable_name" in value:
        out["outputVariableName"] = value["output_variable_name"]
    if "evaluation_score" in value:
        out["evaluationScore"] = value["evaluation_score"]
    if "prediction_explanations" in value:
        import capo_frauddetector.types.prediction_explanations

        out["predictionExplanations"] = (
            capo_frauddetector.types.prediction_explanations.serialize_aws_json_1_1(
                value["prediction_explanations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelVersionEvaluation:
    out: ModelVersionEvaluation = {}  # type: ignore[typeddict-item]
    if "outputVariableName" in data:
        out["output_variable_name"] = data["outputVariableName"]
    if "evaluationScore" in data:
        out["evaluation_score"] = data["evaluationScore"]
    if "predictionExplanations" in data:
        import capo_frauddetector.types.prediction_explanations

        out["prediction_explanations"] = (
            capo_frauddetector.types.prediction_explanations.deserialize_aws_json_1_1(
                data["predictionExplanations"]
            )
        )
    return out
