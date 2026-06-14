"""Generated from Smithy shape ``com.amazonaws.datazone#ListNotebookRunsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.notebook_run_status
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.schedule_id
    import aws_sdk_datazone.types.sort_order


class ListNotebookRunsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebook runs.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook runs.</p>"""
    notebook_identifier: NotRequired["aws_sdk_datazone.types.notebook_id.NotebookId"]
    """<p>The identifier of the notebook to filter runs by.</p>"""
    status: NotRequired["aws_sdk_datazone.types.notebook_run_status.NotebookRunStatus"]
    """<p>The status to filter notebook runs by.</p>"""
    schedule_identifier: NotRequired["aws_sdk_datazone.types.schedule_id.ScheduleId"]
    """<p>The identifier of the schedule to filter notebook runs by.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of notebook runs to return in a single call. When the number of notebook runs exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>The sort order for the results.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of notebook runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebook runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebookRuns</code> to list the next set of notebook runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotebookRunsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotebookRunsInput:
    out: ListNotebookRunsInput = {}  # type: ignore[typeddict-item]
    return out
