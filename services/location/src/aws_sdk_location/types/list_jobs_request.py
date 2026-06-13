"""Generated from Smithy shape ``com.amazonaws.location#ListJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.jobs_filter
    import aws_sdk_location.types.large_token


class ListJobsRequest(TypedDict):
    filter: NotRequired["aws_sdk_location.types.jobs_filter.JobsFilter"]
    """<p>An optional structure containing criteria by which to filter job results.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of jobs to return.</p>"""
    next_token: NotRequired["aws_sdk_location.types.large_token.LargeToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_location.types.jobs_filter

        out["Filter"] = aws_sdk_location.types.jobs_filter.serialize_json(
            value["filter"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsRequest:
    out: ListJobsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_location.types.jobs_filter

        out["filter"] = aws_sdk_location.types.jobs_filter.deserialize_json(
            data["Filter"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
