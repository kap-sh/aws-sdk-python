"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceImagesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspace_image_list


class DescribeWorkspaceImagesResult(TypedDict, closed=True):
    images: NotRequired["capo_workspaces.types.workspace_image_list.WorkspaceImageList"]
    """<p>Information about the images.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceImagesResult) -> dict:
    out: dict = {}
    if "images" in value:
        import capo_workspaces.types.workspace_image_list

        out["Images"] = (
            capo_workspaces.types.workspace_image_list.serialize_aws_json_1_1(
                value["images"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceImagesResult:
    out: DescribeWorkspaceImagesResult = {}  # type: ignore[typeddict-item]
    if "Images" in data:
        import capo_workspaces.types.workspace_image_list

        out["images"] = (
            capo_workspaces.types.workspace_image_list.deserialize_aws_json_1_1(
                data["Images"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
