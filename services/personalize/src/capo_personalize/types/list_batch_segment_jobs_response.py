"""Generated from Smithy shape ``com.amazonaws.personalize#ListBatchSegmentJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.batch_segment_jobs
    import capo_personalize.types.next_token


class ListBatchSegmentJobsResponse(TypedDict, closed=True):
    batch_segment_jobs: NotRequired[
        "capo_personalize.types.batch_segment_jobs.BatchSegmentJobs"
    ]
    """<p>A list containing information on each job that is returned.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBatchSegmentJobsResponse) -> dict:
    out: dict = {}
    if "batch_segment_jobs" in value:
        import capo_personalize.types.batch_segment_jobs

        out["batchSegmentJobs"] = (
            capo_personalize.types.batch_segment_jobs.serialize_aws_json_1_1(
                value["batch_segment_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBatchSegmentJobsResponse:
    out: ListBatchSegmentJobsResponse = {}  # type: ignore[typeddict-item]
    if "batchSegmentJobs" in data:
        import capo_personalize.types.batch_segment_jobs

        out["batch_segment_jobs"] = (
            capo_personalize.types.batch_segment_jobs.deserialize_aws_json_1_1(
                data["batchSegmentJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
