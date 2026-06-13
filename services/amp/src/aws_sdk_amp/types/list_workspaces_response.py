"""Generated from Smithy shape ``com.amazonaws.amp#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.pagination_token
    import aws_sdk_amp.types.workspace_summary_list


class ListWorkspacesResponse(TypedDict):
    workspaces: "aws_sdk_amp.types.workspace_summary_list.WorkspaceSummaryList"
    """<p>An array of <code>WorkspaceSummary</code> structures containing information about the workspaces requested.</p>"""
    next_token: NotRequired["aws_sdk_amp.types.pagination_token.PaginationToken"]
    """<p>A token indicating that there are more results to retrieve. You can use this token as part of your next <code>ListWorkspaces</code> request to retrieve those results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.workspace_summary_list

    out["workspaces"] = aws_sdk_amp.types.workspace_summary_list.serialize_json(
        value["workspaces"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if "workspaces" in data:
        import aws_sdk_amp.types.workspace_summary_list

        out["workspaces"] = aws_sdk_amp.types.workspace_summary_list.deserialize_json(
            data["workspaces"]
        )
    else:
        raise DeserializationError("ListWorkspacesResponse.workspaces required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
