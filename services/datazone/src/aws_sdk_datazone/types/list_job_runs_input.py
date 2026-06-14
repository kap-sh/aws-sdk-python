"""Generated from Smithy shape ``com.amazonaws.datazone#ListJobRunsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.job_run_status
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.sort_order


class ListJobRunsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list job runs.</p>"""
    job_identifier: "str"
    """<p>The ID of the job run.</p>"""
    status: NotRequired["aws_sdk_datazone.types.job_run_status.JobRunStatus"]
    """<p>The status of a job run.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>Specifies the order in which job runs are to be sorted.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of job runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of job runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListJobRuns to list the next set of job runs.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of job runs to return in a single call to ListJobRuns. When the number of job runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListJobRuns to list the next set of job runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobRunsInput:
    out: ListJobRunsInput = {}  # type: ignore[typeddict-item]
    return out
