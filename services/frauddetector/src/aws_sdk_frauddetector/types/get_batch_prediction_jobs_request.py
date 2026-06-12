"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetBatchPredictionJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.batch_predictions_max_page_size
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.string


class GetBatchPredictionJobsRequest(TypedDict):
    job_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The batch prediction job for which to get the details.</p>"""
    max_results: NotRequired[
        "aws_sdk_frauddetector.types.batch_predictions_max_page_size.batchPredictionsMaxPageSize"
    ]
    """<p>The maximum number of objects to return for the request.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next token from the previous request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBatchPredictionJobsRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBatchPredictionJobsRequest:
    out: GetBatchPredictionJobsRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
