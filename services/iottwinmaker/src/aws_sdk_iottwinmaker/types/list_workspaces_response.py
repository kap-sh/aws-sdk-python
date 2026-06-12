"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.workspace_summaries


class ListWorkspacesResponse(TypedDict):
    workspace_summaries: NotRequired[
        "aws_sdk_iottwinmaker.types.workspace_summaries.WorkspaceSummaries"
    ]
    """<p>A list of objects that contain information about the workspaces.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    if "workspace_summaries" in value:
        import aws_sdk_iottwinmaker.types.workspace_summaries

        out["workspaceSummaries"] = (
            aws_sdk_iottwinmaker.types.workspace_summaries.serialize_json(
                value["workspace_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if "workspaceSummaries" in data:
        import aws_sdk_iottwinmaker.types.workspace_summaries

        out["workspace_summaries"] = (
            aws_sdk_iottwinmaker.types.workspace_summaries.deserialize_json(
                data["workspaceSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
