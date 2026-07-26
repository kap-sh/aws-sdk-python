"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListFindingsReportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.max_results
    import capo_codeguruprofiler.types.pagination_token
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.timestamp


class ListFindingsReportsRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group from which to search for analysis data.</p>"""
    start_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    end_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The end time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    next_token: NotRequired[
        "capo_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListFindingsReportsRequest</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_codeguruprofiler.types.max_results.MaxResults"]
    """<p>The maximum number of report results returned by <code>ListFindingsReports</code> in paginated output. When this parameter is used, <code>ListFindingsReports</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListFindingsReports</code> request with the returned <code>nextToken</code> value.</p>"""
    daily_reports_only: NotRequired["bool"]
    """<p>A <code>Boolean</code> value indicating whether to only return reports from daily profiles. If set to <code>True</code>, only analysis data from daily profiles is returned. If set to <code>False</code>, analysis data is returned from smaller time windows (for example, one hour).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFindingsReportsRequest:
    out: ListFindingsReportsRequest = {}  # type: ignore[typeddict-item]
    return out
