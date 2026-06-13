"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.link_sharing_configuration
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.update_resource_permission_list


class DescribeDashboardPermissionsResponse(TypedDict):
    dashboard_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the dashboard.</p>"""
    dashboard_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dashboard.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A structure that contains the permissions for the dashboard.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    link_sharing_configuration: NotRequired[
        "aws_sdk_quicksight.types.link_sharing_configuration.LinkSharingConfiguration"
    ]
    """<p>A structure that contains the configuration of a shareable link that grants access to the dashboard. Your users can use the link to view and interact with the dashboard, if the dashboard has been shared with them. For more information about sharing dashboards, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/sharing-a-dashboard.html\">Sharing Dashboards</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardPermissionsResponse) -> dict:
    out: dict = {}
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "link_sharing_configuration" in value:
        import aws_sdk_quicksight.types.link_sharing_configuration

        out["LinkSharingConfiguration"] = (
            aws_sdk_quicksight.types.link_sharing_configuration.serialize_json(
                value["link_sharing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDashboardPermissionsResponse:
    out: DescribeDashboardPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    if "DashboardArn" in data:
        out["dashboard_arn"] = data["DashboardArn"]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "LinkSharingConfiguration" in data:
        import aws_sdk_quicksight.types.link_sharing_configuration

        out["link_sharing_configuration"] = (
            aws_sdk_quicksight.types.link_sharing_configuration.deserialize_json(
                data["LinkSharingConfiguration"]
            )
        )
    return out
