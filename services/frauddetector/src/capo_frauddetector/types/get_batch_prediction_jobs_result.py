"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetBatchPredictionJobsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_prediction_list
    import capo_frauddetector.types.string


class GetBatchPredictionJobsResult(TypedDict, closed=True):
    batch_predictions: NotRequired[
        "capo_frauddetector.types.batch_prediction_list.BatchPredictionList"
    ]
    """<p>An array containing the details of each batch prediction job.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token for the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBatchPredictionJobsResult) -> dict:
    out: dict = {}
    if "batch_predictions" in value:
        import capo_frauddetector.types.batch_prediction_list

        out["batchPredictions"] = (
            capo_frauddetector.types.batch_prediction_list.serialize_aws_json_1_1(
                value["batch_predictions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBatchPredictionJobsResult:
    out: GetBatchPredictionJobsResult = {}  # type: ignore[typeddict-item]
    if "batchPredictions" in data:
        import capo_frauddetector.types.batch_prediction_list

        out["batch_predictions"] = (
            capo_frauddetector.types.batch_prediction_list.deserialize_aws_json_1_1(
                data["batchPredictions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
