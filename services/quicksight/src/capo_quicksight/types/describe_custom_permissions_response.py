"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeCustomPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_permissions
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeCustomPermissionsResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    custom_permissions: NotRequired[
        "capo_quicksight.types.custom_permissions.CustomPermissions"
    ]
    """<p>The custom permissions profile.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomPermissionsResponse) -> dict:
    out: dict = {}
    out["Status"] = value.get("status", 0)
    if "custom_permissions" in value:
        import capo_quicksight.types.custom_permissions

        out["CustomPermissions"] = (
            capo_quicksight.types.custom_permissions.serialize_json(
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
        import capo_quicksight.types.custom_permissions

        out["custom_permissions"] = (
            capo_quicksight.types.custom_permissions.deserialize_json(
                data["CustomPermissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
