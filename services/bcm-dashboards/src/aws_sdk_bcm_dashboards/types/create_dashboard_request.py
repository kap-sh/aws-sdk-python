"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CreateDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dashboard_name
    import aws_sdk_bcm_dashboards.types.description
    import aws_sdk_bcm_dashboards.types.resource_tag_list
    import aws_sdk_bcm_dashboards.types.widget_list


class CreateDashboardRequest(TypedDict, closed=True):
    name: "aws_sdk_bcm_dashboards.types.dashboard_name.DashboardName"
    """<p>The name of the dashboard. The name must be unique within your account.</p>"""
    description: NotRequired["aws_sdk_bcm_dashboards.types.description.Description"]
    """<p>A description of the dashboard's purpose or contents.</p>"""
    widgets: "aws_sdk_bcm_dashboards.types.widget_list.WidgetList"
    """<p>An array of widget configurations that define the visualizations to be displayed in the dashboard. Each dashboard can contain up to 20 widgets.</p>"""
    resource_tags: NotRequired[
        "aws_sdk_bcm_dashboards.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The tags to apply to the dashboard resource for organization and management.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDashboardRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bcm_dashboards.types.widget_list

    out["widgets"] = aws_sdk_bcm_dashboards.types.widget_list.serialize_aws_json_1_0(
        value["widgets"]
    )
    if "resource_tags" in value:
        import aws_sdk_bcm_dashboards.types.resource_tag_list

        out["resourceTags"] = (
            aws_sdk_bcm_dashboards.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDashboardRequest:
    out: CreateDashboardRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDashboardRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "widgets" in data:
        import aws_sdk_bcm_dashboards.types.widget_list

        out["widgets"] = (
            aws_sdk_bcm_dashboards.types.widget_list.deserialize_aws_json_1_0(
                data["widgets"]
            )
        )
    else:
        raise DeserializationError("CreateDashboardRequest.widgets required")
    if "resourceTags" in data:
        import aws_sdk_bcm_dashboards.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_bcm_dashboards.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
