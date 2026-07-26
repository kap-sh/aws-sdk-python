"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateBatchPredictionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class UpdateBatchPredictionOutput(TypedDict, closed=True):
    batch_prediction_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>The ID assigned to the <code>BatchPrediction</code> during creation. This value should be identical to the value of the <code>BatchPredictionId</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBatchPredictionOutput) -> dict:
    out: dict = {}
    if "batch_prediction_id" in value:
        out["BatchPredictionId"] = value["batch_prediction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBatchPredictionOutput:
    out: UpdateBatchPredictionOutput = {}  # type: ignore[typeddict-item]
    if "BatchPredictionId" in data:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    return out
