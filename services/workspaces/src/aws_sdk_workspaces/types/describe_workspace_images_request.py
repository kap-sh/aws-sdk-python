"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceImagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.image_type
    import aws_sdk_workspaces.types.limit
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspace_image_id_list


class DescribeWorkspaceImagesRequest(TypedDict):
    image_ids: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_id_list.WorkspaceImageIdList"
    ]
    """<p>The identifier of the image.</p>"""
    image_type: NotRequired["aws_sdk_workspaces.types.image_type.ImageType"]
    """<p>The type (owned or shared) of the image.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_workspaces.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceImagesRequest) -> dict:
    out: dict = {}
    if "image_ids" in value:
        import aws_sdk_workspaces.types.workspace_image_id_list

        out["ImageIds"] = (
            aws_sdk_workspaces.types.workspace_image_id_list.serialize_aws_json_1_1(
                value["image_ids"]
            )
        )
    if "image_type" in value:
        import aws_sdk_workspaces.types.image_type

        out["ImageType"] = aws_sdk_workspaces.types.image_type.serialize_aws_json_1_1(
            value["image_type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceImagesRequest:
    out: DescribeWorkspaceImagesRequest = {}  # type: ignore[typeddict-item]
    if "ImageIds" in data:
        import aws_sdk_workspaces.types.workspace_image_id_list

        out["image_ids"] = (
            aws_sdk_workspaces.types.workspace_image_id_list.deserialize_aws_json_1_1(
                data["ImageIds"]
            )
        )
    if "ImageType" in data:
        import aws_sdk_workspaces.types.image_type

        out["image_type"] = (
            aws_sdk_workspaces.types.image_type.deserialize_aws_json_1_1(
                data["ImageType"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
