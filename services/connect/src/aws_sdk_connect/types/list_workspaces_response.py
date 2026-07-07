"""Generated from Smithy shape ``com.amazonaws.connect#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.workspace_summary_list


class ListWorkspacesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    workspace_summary_list: (
        "aws_sdk_connect.types.workspace_summary_list.WorkspaceSummaryList"
    )
    """<p>A summary list of workspaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_connect.types.workspace_summary_list

    out["WorkspaceSummaryList"] = (
        aws_sdk_connect.types.workspace_summary_list.serialize_json(
            value["workspace_summary_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WorkspaceSummaryList" in data:
        import aws_sdk_connect.types.workspace_summary_list

        out["workspace_summary_list"] = (
            aws_sdk_connect.types.workspace_summary_list.deserialize_json(
                data["WorkspaceSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkspacesResponse.workspace_summary_list required"
        )
    return out
