"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.link_sharing_configuration
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.update_resource_permission_list


class UpdateDashboardPermissionsResponse(TypedDict, closed=True):
    dashboard_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dashboard.</p>"""
    dashboard_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the dashboard.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>Information about the permissions on the dashboard.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    link_sharing_configuration: NotRequired[
        "capo_quicksight.types.link_sharing_configuration.LinkSharingConfiguration"
    ]
    """<p>Updates the permissions of a shared link to an Quick Sight dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardPermissionsResponse) -> dict:
    out: dict = {}
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "permissions" in value:
        import capo_quicksight.types.update_resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.update_resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "link_sharing_configuration" in value:
        import capo_quicksight.types.link_sharing_configuration

        out["LinkSharingConfiguration"] = (
            capo_quicksight.types.link_sharing_configuration.serialize_json(
                value["link_sharing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDashboardPermissionsResponse:
    out: UpdateDashboardPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "DashboardArn" in data:
        out["dashboard_arn"] = data["DashboardArn"]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    if "Permissions" in data:
        import capo_quicksight.types.update_resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.update_resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "LinkSharingConfiguration" in data:
        import capo_quicksight.types.link_sharing_configuration

        out["link_sharing_configuration"] = (
            capo_quicksight.types.link_sharing_configuration.deserialize_json(
                data["LinkSharingConfiguration"]
            )
        )
    return out
