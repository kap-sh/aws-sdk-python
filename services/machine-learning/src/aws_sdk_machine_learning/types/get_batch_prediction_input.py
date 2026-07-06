"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetBatchPredictionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class GetBatchPredictionInput(TypedDict, closed=True):
    batch_prediction_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>An ID assigned to the <code>BatchPrediction</code> at creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBatchPredictionInput) -> dict:
    out: dict = {}
    out["BatchPredictionId"] = value["batch_prediction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBatchPredictionInput:
    out: GetBatchPredictionInput = {}  # type: ignore[typeddict-item]
    if "BatchPredictionId" in data:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    else:
        raise DeserializationError(
            "GetBatchPredictionInput.batch_prediction_id required"
        )
    return out
