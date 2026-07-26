"""Generated from Smithy shape ``com.amazonaws.personalize#ListBatchInferenceJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.batch_inference_jobs
    import capo_personalize.types.next_token


class ListBatchInferenceJobsResponse(TypedDict, closed=True):
    batch_inference_jobs: NotRequired[
        "capo_personalize.types.batch_inference_jobs.BatchInferenceJobs"
    ]
    """<p>A list containing information on each job that is returned.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBatchInferenceJobsResponse) -> dict:
    out: dict = {}
    if "batch_inference_jobs" in value:
        import capo_personalize.types.batch_inference_jobs

        out["batchInferenceJobs"] = (
            capo_personalize.types.batch_inference_jobs.serialize_aws_json_1_1(
                value["batch_inference_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBatchInferenceJobsResponse:
    out: ListBatchInferenceJobsResponse = {}  # type: ignore[typeddict-item]
    if "batchInferenceJobs" in data:
        import capo_personalize.types.batch_inference_jobs

        out["batch_inference_jobs"] = (
            capo_personalize.types.batch_inference_jobs.deserialize_aws_json_1_1(
                data["batchInferenceJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
