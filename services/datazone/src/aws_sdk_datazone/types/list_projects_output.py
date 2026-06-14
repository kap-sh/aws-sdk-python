"""Generated from Smithy shape ``com.amazonaws.datazone#ListProjectsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_summaries


class ListProjectsOutput(TypedDict):
    items: NotRequired["aws_sdk_datazone.types.project_summaries.ProjectSummaries"]
    """<p>The results of the <code>ListProjects</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of projects is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of projects, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjects</code> to list the next set of projects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.project_summaries

        out["items"] = aws_sdk_datazone.types.project_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectsOutput:
    out: ListProjectsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.project_summaries

        out["items"] = aws_sdk_datazone.types.project_summaries.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
