"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateBatchPredictionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class CreateBatchPredictionOutput(TypedDict):
    batch_prediction_id: NotRequired[
        "aws_sdk_machine_learning.types.entity_id.EntityId"
    ]
    """<p>A user-supplied ID that uniquely identifies the <code>BatchPrediction</code>. This value is identical to the value of the <code>BatchPredictionId</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchPredictionOutput) -> dict:
    out: dict = {}
    if "batch_prediction_id" in value:
        out["BatchPredictionId"] = value["batch_prediction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchPredictionOutput:
    out: CreateBatchPredictionOutput = {}  # type: ignore[typeddict-item]
    if "BatchPredictionId" in data:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    return out
