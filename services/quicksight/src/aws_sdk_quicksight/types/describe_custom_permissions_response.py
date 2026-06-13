"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeCustomPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_permissions
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeCustomPermissionsResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    custom_permissions: NotRequired[
        "aws_sdk_quicksight.types.custom_permissions.CustomPermissions"
    ]
    """<p>The custom permissions profile.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomPermissionsResponse) -> dict:
    out: dict = {}
    out["Status"] = value.get("status", 0)
    if "custom_permissions" in value:
        import aws_sdk_quicksight.types.custom_permissions

        out["CustomPermissions"] = (
            aws_sdk_quicksight.types.custom_permissions.serialize_json(
                value["custom_permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeCustomPermissionsResponse:
    out: DescribeCustomPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    if "CustomPermissions" in data:
        import aws_sdk_quicksight.types.custom_permissions

        out["custom_permissions"] = (
            aws_sdk_quicksight.types.custom_permissions.deserialize_json(
                data["CustomPermissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
