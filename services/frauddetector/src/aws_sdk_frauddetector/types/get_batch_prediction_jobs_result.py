"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetBatchPredictionJobsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.batch_prediction_list
    import aws_sdk_frauddetector.types.string


class GetBatchPredictionJobsResult(TypedDict):
    batch_predictions: NotRequired[
        "aws_sdk_frauddetector.types.batch_prediction_list.BatchPredictionList"
    ]
    """<p>An array containing the details of each batch prediction job.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next token for the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBatchPredictionJobsResult) -> dict:
    out: dict = {}
    if "batch_predictions" in value:
        import aws_sdk_frauddetector.types.batch_prediction_list

        out["batchPredictions"] = (
            aws_sdk_frauddetector.types.batch_prediction_list.serialize_aws_json_1_1(
                value["batch_predictions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBatchPredictionJobsResult:
    out: GetBatchPredictionJobsResult = {}  # type: ignore[typeddict-item]
    if "batchPredictions" in data:
        import aws_sdk_frauddetector.types.batch_prediction_list

        out["batch_predictions"] = (
            aws_sdk_frauddetector.types.batch_prediction_list.deserialize_aws_json_1_1(
                data["batchPredictions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
