"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFoldersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.folder_summary_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class SearchFoldersResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folder_summary_list: NotRequired[
        "capo_quicksight.types.folder_summary_list.FolderSummaryList"
    ]
    """<p>A structure that contains all of the folders in the Amazon Web Services account. This structure provides basic information about the folders.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFoldersResponse) -> dict:
    out: dict = {}
    if "folder_summary_list" in value:
        import capo_quicksight.types.folder_summary_list

        out["FolderSummaryList"] = (
            capo_quicksight.types.folder_summary_list.serialize_json(
                value["folder_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchFoldersResponse:
    out: SearchFoldersResponse = {}  # type: ignore[typeddict-item]
    if "FolderSummaryList" in data:
        import capo_quicksight.types.folder_summary_list

        out["folder_summary_list"] = (
            capo_quicksight.types.folder_summary_list.deserialize_json(
                data["FolderSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
