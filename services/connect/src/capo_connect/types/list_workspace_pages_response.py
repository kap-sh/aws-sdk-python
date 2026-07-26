"""Generated from Smithy shape ``com.amazonaws.connect#ListWorkspacePagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.workspace_page_list


class ListWorkspacePagesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    workspace_page_list: "capo_connect.types.workspace_page_list.WorkspacePageList"
    """<p>A list of page configurations in the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacePagesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_connect.types.workspace_page_list

    out["WorkspacePageList"] = capo_connect.types.workspace_page_list.serialize_json(
        value["workspace_page_list"]
    )
    return out


def deserialize_json(data: dict) -> ListWorkspacePagesResponse:
    out: ListWorkspacePagesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WorkspacePageList" in data:
        import capo_connect.types.workspace_page_list

        out["workspace_page_list"] = (
            capo_connect.types.workspace_page_list.deserialize_json(
                data["WorkspacePageList"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkspacePagesResponse.workspace_page_list required"
        )
    return out
