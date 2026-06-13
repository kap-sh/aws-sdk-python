"""Generated from Smithy shape ``com.amazonaws.quicksight#ListFoldersForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.folders_for_resource_arn_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListFoldersForResourceResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folders: NotRequired[
        "aws_sdk_quicksight.types.folders_for_resource_arn_list.FoldersForResourceArnList"
    ]
    """<p>A list that contains the Amazon Resource Names (ARNs) of all folders that the resource is a member of.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFoldersForResourceResponse) -> dict:
    out: dict = {}
    if "folders" in value:
        import aws_sdk_quicksight.types.folders_for_resource_arn_list

        out["Folders"] = (
            aws_sdk_quicksight.types.folders_for_resource_arn_list.serialize_json(
                value["folders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListFoldersForResourceResponse:
    out: ListFoldersForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Folders" in data:
        import aws_sdk_quicksight.types.folders_for_resource_arn_list

        out["folders"] = (
            aws_sdk_quicksight.types.folders_for_resource_arn_list.deserialize_json(
                data["Folders"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
