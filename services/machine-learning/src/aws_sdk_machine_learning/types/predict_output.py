"""Generated from Smithy shape ``com.amazonaws.machinelearning#PredictOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.prediction


class PredictOutput(TypedDict):
    prediction: NotRequired["aws_sdk_machine_learning.types.prediction.Prediction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictOutput) -> dict:
    out: dict = {}
    if "prediction" in value:
        import aws_sdk_machine_learning.types.prediction

        out["Prediction"] = (
            aws_sdk_machine_learning.types.prediction.serialize_aws_json_1_1(
                value["prediction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictOutput:
    out: PredictOutput = {}  # type: ignore[typeddict-item]
    if "Prediction" in data:
        import aws_sdk_machine_learning.types.prediction

        out["prediction"] = (
            aws_sdk_machine_learning.types.prediction.deserialize_aws_json_1_1(
                data["Prediction"]
            )
        )
    return out
