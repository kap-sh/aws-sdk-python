"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeRoleCustomPermissionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.role_name
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeRoleCustomPermissionResponse(TypedDict):
    custom_permissions_name: NotRequired["aws_sdk_quicksight.types.role_name.RoleName"]
    """<p>The name of the custom permission that is described.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRoleCustomPermissionResponse) -> dict:
    out: dict = {}
    if "custom_permissions_name" in value:
        out["CustomPermissionsName"] = value["custom_permissions_name"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    out["Status"] = value.get("status", 0)
    return out


def deserialize_json(data: dict) -> DescribeRoleCustomPermissionResponse:
    out: DescribeRoleCustomPermissionResponse = {}  # type: ignore[typeddict-item]
    if "CustomPermissionsName" in data:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    return out
