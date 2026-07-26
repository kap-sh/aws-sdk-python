"""Generated from Smithy shape ``com.amazonaws.machinelearning#PredictOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.prediction


class PredictOutput(TypedDict, closed=True):
    prediction: NotRequired["capo_machine_learning.types.prediction.Prediction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictOutput) -> dict:
    out: dict = {}
    if "prediction" in value:
        import capo_machine_learning.types.prediction

        out["Prediction"] = (
            capo_machine_learning.types.prediction.serialize_aws_json_1_1(
                value["prediction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictOutput:
    out: PredictOutput = {}  # type: ignore[typeddict-item]
    if "Prediction" in data:
        import capo_machine_learning.types.prediction

        out["prediction"] = (
            capo_machine_learning.types.prediction.deserialize_aws_json_1_1(
                data["Prediction"]
            )
        )
    return out
