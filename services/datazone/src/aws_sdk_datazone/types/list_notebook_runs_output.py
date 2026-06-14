"""Generated from Smithy shape ``com.amazonaws.datazone#ListNotebookRunsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.notebook_run_summary_list
    import aws_sdk_datazone.types.pagination_token


class ListNotebookRunsOutput(TypedDict):
    items: NotRequired[
        "aws_sdk_datazone.types.notebook_run_summary_list.NotebookRunSummaryList"
    ]
    """<p>The results of the <code>ListNotebookRuns</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of notebook runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebook runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebookRuns</code> to list the next set of notebook runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotebookRunsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.notebook_run_summary_list

        out["items"] = aws_sdk_datazone.types.notebook_run_summary_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotebookRunsOutput:
    out: ListNotebookRunsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.notebook_run_summary_list

        out["items"] = (
            aws_sdk_datazone.types.notebook_run_summary_list.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
