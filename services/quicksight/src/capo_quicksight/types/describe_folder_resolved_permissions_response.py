"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFolderResolvedPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeFolderResolvedPermissionsResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folder_id: NotRequired[
        "capo_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of the folder.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the folder.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>Information about the permissions for the folder.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderResolvedPermissionsResponse) -> dict:
    out: dict = {}
    if "folder_id" in value:
        out["FolderId"] = value["folder_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeFolderResolvedPermissionsResponse:
    out: DescribeFolderResolvedPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "FolderId" in data:
        out["folder_id"] = data["FolderId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Permissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
