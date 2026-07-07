"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteBatchPredictionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class DeleteBatchPredictionOutput(TypedDict, closed=True):
    batch_prediction_id: NotRequired[
        "aws_sdk_machine_learning.types.entity_id.EntityId"
    ]
    """<p>A user-supplied ID that uniquely identifies the <code>BatchPrediction</code>. This value should be identical to the value of the <code>BatchPredictionID</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBatchPredictionOutput) -> dict:
    out: dict = {}
    if "batch_prediction_id" in value:
        out["BatchPredictionId"] = value["batch_prediction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBatchPredictionOutput:
    out: DeleteBatchPredictionOutput = {}  # type: ignore[typeddict-item]
    if "BatchPredictionId" in data:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    return out
