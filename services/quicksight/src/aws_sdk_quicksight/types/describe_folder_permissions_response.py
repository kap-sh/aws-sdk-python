"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFolderPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeFolderPermissionsResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folder_id: NotRequired[
        "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of the folder.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the folder.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>Information about the permissions on the folder.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The pagination token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderPermissionsResponse) -> dict:
    out: dict = {}
    if "folder_id" in value:
        out["FolderId"] = value["folder_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeFolderPermissionsResponse:
    out: DescribeFolderPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "FolderId" in data:
        out["folder_id"] = data["FolderId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
