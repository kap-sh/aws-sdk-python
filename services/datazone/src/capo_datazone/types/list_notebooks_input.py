"""Generated from Smithy shape ``com.amazonaws.datazone#ListNotebooksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.max_results
    import capo_datazone.types.notebook_status
    import capo_datazone.types.pagination_token
    import capo_datazone.types.project_id
    import capo_datazone.types.sort_key
    import capo_datazone.types.sort_order


class ListNotebooksInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebooks.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebooks.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of notebooks to return in a single call. When the number of notebooks exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>"""
    sort_order: NotRequired["capo_datazone.types.sort_order.SortOrder"]
    """<p>The sort order for the results.</p>"""
    sort_by: NotRequired["capo_datazone.types.sort_key.SortKey"]
    """<p>The field to sort the results by.</p>"""
    status: NotRequired["capo_datazone.types.notebook_status.NotebookStatus"]
    """<p>The status to filter notebooks by.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of notebooks is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebooks, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebooks</code> to list the next set of notebooks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotebooksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotebooksInput:
    out: ListNotebooksInput = {}  # type: ignore[typeddict-item]
    return out
