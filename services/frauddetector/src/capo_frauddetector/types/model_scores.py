"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelScores``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.model_prediction_map
    import capo_frauddetector.types.model_version


class ModelScores(TypedDict, closed=True):
    model_version: NotRequired["capo_frauddetector.types.model_version.ModelVersion"]
    """<p>The model version.</p>"""
    scores: NotRequired[
        "capo_frauddetector.types.model_prediction_map.ModelPredictionMap"
    ]
    """<p>The model's fraud prediction scores.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelScores) -> dict:
    out: dict = {}
    if "model_version" in value:
        import capo_frauddetector.types.model_version

        out["modelVersion"] = (
            capo_frauddetector.types.model_version.serialize_aws_json_1_1(
                value["model_version"]
            )
        )
    if "scores" in value:
        import capo_frauddetector.types.model_prediction_map

        out["scores"] = (
            capo_frauddetector.types.model_prediction_map.serialize_aws_json_1_1(
                value["scores"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelScores:
    out: ModelScores = {}  # type: ignore[typeddict-item]
    if "modelVersion" in data:
        import capo_frauddetector.types.model_version

        out["model_version"] = (
            capo_frauddetector.types.model_version.deserialize_aws_json_1_1(
                data["modelVersion"]
            )
        )
    if "scores" in data:
        import capo_frauddetector.types.model_prediction_map

        out["scores"] = (
            capo_frauddetector.types.model_prediction_map.deserialize_aws_json_1_1(
                data["scores"]
            )
        )
    return out
