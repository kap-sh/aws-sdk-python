"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceImagePermissionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.image_permissions
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspace_image_id


class DescribeWorkspaceImagePermissionsResult(TypedDict, closed=True):
    image_id: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    ]
    """<p>The identifier of the image.</p>"""
    image_permissions: NotRequired[
        "aws_sdk_workspaces.types.image_permissions.ImagePermissions"
    ]
    """<p>The identifiers of the Amazon Web Services accounts that the image has been shared with.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceImagePermissionsResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "image_permissions" in value:
        import aws_sdk_workspaces.types.image_permissions

        out["ImagePermissions"] = (
            aws_sdk_workspaces.types.image_permissions.serialize_aws_json_1_1(
                value["image_permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceImagePermissionsResult:
    out: DescribeWorkspaceImagePermissionsResult = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "ImagePermissions" in data:
        import aws_sdk_workspaces.types.image_permissions

        out["image_permissions"] = (
            aws_sdk_workspaces.types.image_permissions.deserialize_aws_json_1_1(
                data["ImagePermissions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
