"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GetDashboardResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dashboard_arn
    import aws_sdk_bcm_dashboards.types.dashboard_name
    import aws_sdk_bcm_dashboards.types.dashboard_type
    import aws_sdk_bcm_dashboards.types.description
    import aws_sdk_bcm_dashboards.types.generic_time_stamp
    import aws_sdk_bcm_dashboards.types.widget_list


class GetDashboardResponse(TypedDict):
    arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the retrieved dashboard.</p>"""
    name: "aws_sdk_bcm_dashboards.types.dashboard_name.DashboardName"
    """<p>The name of the retrieved dashboard.</p>"""
    description: NotRequired["aws_sdk_bcm_dashboards.types.description.Description"]
    """<p>The description of the retrieved dashboard.</p>"""
    type: "aws_sdk_bcm_dashboards.types.dashboard_type.DashboardType"
    """<p>Indicates the dashboard type.</p>"""
    widgets: "aws_sdk_bcm_dashboards.types.widget_list.WidgetList"
    """<p>An array of widget configurations that make up the dashboard.</p>"""
    created_at: "aws_sdk_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    """<p>The timestamp when the dashboard was created.</p>"""
    updated_at: "aws_sdk_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    """<p>The timestamp when the dashboard was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDashboardResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bcm_dashboards.types.dashboard_type

    out["type"] = aws_sdk_bcm_dashboards.types.dashboard_type.serialize_aws_json_1_0(
        value["type"]
    )
    import aws_sdk_bcm_dashboards.types.widget_list

    out["widgets"] = aws_sdk_bcm_dashboards.types.widget_list.serialize_aws_json_1_0(
        value["widgets"]
    )
    import aws_sdk_bcm_dashboards.types.generic_time_stamp

    out["createdAt"] = (
        aws_sdk_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import aws_sdk_bcm_dashboards.types.generic_time_stamp

    out["updatedAt"] = (
        aws_sdk_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDashboardResponse:
    out: GetDashboardResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetDashboardResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetDashboardResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_bcm_dashboards.types.dashboard_type

        out["type"] = (
            aws_sdk_bcm_dashboards.types.dashboard_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        raise DeserializationError("GetDashboardResponse.type required")
    if "widgets" in data:
        import aws_sdk_bcm_dashboards.types.widget_list

        out["widgets"] = (
            aws_sdk_bcm_dashboards.types.widget_list.deserialize_aws_json_1_0(
                data["widgets"]
            )
        )
    else:
        raise DeserializationError("GetDashboardResponse.widgets required")
    if "createdAt" in data:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["created_at"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetDashboardResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["updated_at"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetDashboardResponse.updated_at required")
    return out
