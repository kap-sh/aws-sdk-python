"""Generated from Smithy shape ``com.amazonaws.datazone#ListDataSourceRunsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_run_status
    import capo_datazone.types.domain_id
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token


class ListDataSourceRunsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which to invoke the <code>ListDataSourceRuns</code> action.</p>"""
    data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source.</p>"""
    status: NotRequired[
        "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
    ]
    """<p>The status of the data source.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of runs to return in a single call to <code>ListDataSourceRuns</code>. When the number of runs to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourceRunsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSourceRunsInput:
    out: ListDataSourceRunsInput = {}  # type: ignore[typeddict-item]
    return out
