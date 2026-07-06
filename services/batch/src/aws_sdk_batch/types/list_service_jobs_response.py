"""Generated from Smithy shape ``com.amazonaws.batch#ListServiceJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.service_job_summary_list
    import aws_sdk_batch.types.string


class ListServiceJobsResponse(TypedDict, closed=True):
    job_summary_list: NotRequired[
        "aws_sdk_batch.types.service_job_summary_list.ServiceJobSummaryList"
    ]
    """<p>A list of service job summaries.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListServiceJobs</code> request. When the results of a <code>ListServiceJobs</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceJobsResponse) -> dict:
    out: dict = {}
    if "job_summary_list" in value:
        import aws_sdk_batch.types.service_job_summary_list

        out["jobSummaryList"] = (
            aws_sdk_batch.types.service_job_summary_list.serialize_json(
                value["job_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceJobsResponse:
    out: ListServiceJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobSummaryList" in data:
        import aws_sdk_batch.types.service_job_summary_list

        out["job_summary_list"] = (
            aws_sdk_batch.types.service_job_summary_list.deserialize_json(
                data["jobSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
