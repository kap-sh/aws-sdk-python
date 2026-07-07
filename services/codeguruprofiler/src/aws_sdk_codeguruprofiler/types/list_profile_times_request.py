"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListProfileTimesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.aggregation_period
    import aws_sdk_codeguruprofiler.types.max_results
    import aws_sdk_codeguruprofiler.types.order_by
    import aws_sdk_codeguruprofiler.types.pagination_token
    import aws_sdk_codeguruprofiler.types.profiling_group_name
    import aws_sdk_codeguruprofiler.types.timestamp


class ListProfileTimesRequest(TypedDict, closed=True):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group.</p>"""
    start_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p>The start time of the time range from which to list the profiles.</p>"""
    end_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p>The end time of the time range from which to list the profiles.</p>"""
    period: "aws_sdk_codeguruprofiler.types.aggregation_period.AggregationPeriod"
    """<p> The aggregation period. This specifies the period during which an aggregation profile collects posted agent profiles for a profiling group. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>"""
    order_by: NotRequired["aws_sdk_codeguruprofiler.types.order_by.OrderBy"]
    """<p>The order (ascending or descending by start time of the profile) to use when listing profiles. Defaults to <code>TIMESTAMP_DESCENDING</code>. </p>"""
    max_results: NotRequired["aws_sdk_codeguruprofiler.types.max_results.MaxResults"]
    """<p>The maximum number of profile time results returned by <code>ListProfileTimes</code> in paginated output. When this parameter is used, <code>ListProfileTimes</code> only returns <code>maxResults</code> results in a single page with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListProfileTimes</code> request with the returned <code>nextToken</code> value. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListProfileTimes</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileTimesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfileTimesRequest:
    out: ListProfileTimesRequest = {}  # type: ignore[typeddict-item]
    return out
