"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetFindingsReportAccountSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.max_results
    import capo_codeguruprofiler.types.pagination_token


class GetFindingsReportAccountSummaryRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>GetFindingsReportAccountSummary</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_codeguruprofiler.types.max_results.MaxResults"]
    """<p>The maximum number of results returned by <code> GetFindingsReportAccountSummary</code> in paginated output. When this parameter is used, <code>GetFindingsReportAccountSummary</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetFindingsReportAccountSummary</code> request with the returned <code>nextToken</code> value.</p>"""
    daily_reports_only: NotRequired["bool"]
    """<p>A <code>Boolean</code> value indicating whether to only return reports from daily profiles. If set to <code>True</code>, only analysis data from daily profiles is returned. If set to <code>False</code>, analysis data is returned from smaller time windows (for example, one hour).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsReportAccountSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFindingsReportAccountSummaryRequest:
    out: GetFindingsReportAccountSummaryRequest = {}  # type: ignore[typeddict-item]
    return out
