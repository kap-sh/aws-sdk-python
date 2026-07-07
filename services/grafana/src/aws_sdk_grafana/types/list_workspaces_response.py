"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.workspace_list


class ListWorkspacesResponse(TypedDict, closed=True):
    workspaces: "aws_sdk_grafana.types.workspace_list.WorkspaceList"
    """<p>An array of structures that contain some information about the workspaces in the account.</p>"""
    next_token: NotRequired["aws_sdk_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of workspaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.workspace_list

    out["workspaces"] = aws_sdk_grafana.types.workspace_list.serialize_json(
        value["workspaces"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if "workspaces" in data:
        import aws_sdk_grafana.types.workspace_list

        out["workspaces"] = aws_sdk_grafana.types.workspace_list.deserialize_json(
            data["workspaces"]
        )
    else:
        raise DeserializationError("ListWorkspacesResponse.workspaces required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
