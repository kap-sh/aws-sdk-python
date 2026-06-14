"""Generated from Smithy shape ``com.amazonaws.datazone#ListNotebooksOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.notebook_summary_list
    import aws_sdk_datazone.types.pagination_token


class ListNotebooksOutput(TypedDict):
    items: NotRequired[
        "aws_sdk_datazone.types.notebook_summary_list.NotebookSummaryList"
    ]
    """<p>The results of the <code>ListNotebooks</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of notebooks is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebooks, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebooks</code> to list the next set of notebooks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotebooksOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.notebook_summary_list

        out["items"] = aws_sdk_datazone.types.notebook_summary_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotebooksOutput:
    out: ListNotebooksOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.notebook_summary_list

        out["items"] = aws_sdk_datazone.types.notebook_summary_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
