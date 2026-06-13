"""Generated from Smithy shape ``com.amazonaws.datazone#ListJobRunsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.job_run_summaries
    import aws_sdk_datazone.types.pagination_token


class ListJobRunsOutput(TypedDict):
    items: NotRequired["aws_sdk_datazone.types.job_run_summaries.JobRunSummaries"]
    """<p>The results of the ListJobRuns action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of job runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of job runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListJobRuns to list the next set of job runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.job_run_summaries

        out["items"] = aws_sdk_datazone.types.job_run_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobRunsOutput:
    out: ListJobRunsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.job_run_summaries

        out["items"] = aws_sdk_datazone.types.job_run_summaries.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
