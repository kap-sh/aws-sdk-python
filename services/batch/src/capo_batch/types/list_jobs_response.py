"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.job_summary_list
    import capo_batch.types.string


class ListJobsResponse(TypedDict, closed=True):
    job_summary_list: NotRequired["capo_batch.types.job_summary_list.JobSummaryList"]
    """<p>A list of job summaries that match the request.</p>"""
    next_token: NotRequired["capo_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListJobs</code> request. When the results of a <code>ListJobs</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    if "job_summary_list" in value:
        import capo_batch.types.job_summary_list

        out["jobSummaryList"] = capo_batch.types.job_summary_list.serialize_json(
            value["job_summary_list"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobSummaryList" in data:
        import capo_batch.types.job_summary_list

        out["job_summary_list"] = capo_batch.types.job_summary_list.deserialize_json(
            data["jobSummaryList"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
