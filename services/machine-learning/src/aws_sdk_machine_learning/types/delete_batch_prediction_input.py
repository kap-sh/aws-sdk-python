"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteBatchPredictionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class DeleteBatchPredictionInput(TypedDict):
    batch_prediction_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>BatchPrediction</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBatchPredictionInput) -> dict:
    out: dict = {}
    out["BatchPredictionId"] = value["batch_prediction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBatchPredictionInput:
    out: DeleteBatchPredictionInput = {}  # type: ignore[typeddict-item]
    if "BatchPredictionId" in data:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    else:
        raise DeserializationError(
            "DeleteBatchPredictionInput.batch_prediction_id required"
        )
    return out
