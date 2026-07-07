"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.dashboard_arn
    import aws_sdk_cloudtrail.types.dashboard_name
    import aws_sdk_cloudtrail.types.dashboard_type
    import aws_sdk_cloudtrail.types.refresh_schedule
    import aws_sdk_cloudtrail.types.tags_list
    import aws_sdk_cloudtrail.types.termination_protection_enabled
    import aws_sdk_cloudtrail.types.widget_list


class CreateDashboardResponse(TypedDict, closed=True):
    dashboard_arn: NotRequired["aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn"]
    """<p> The ARN for the dashboard. </p>"""
    name: NotRequired["aws_sdk_cloudtrail.types.dashboard_name.DashboardName"]
    """<p> The name of the dashboard. </p>"""
    type: NotRequired["aws_sdk_cloudtrail.types.dashboard_type.DashboardType"]
    """<p> The dashboard type. </p>"""
    widgets: NotRequired["aws_sdk_cloudtrail.types.widget_list.WidgetList"]
    """<p> An array of widgets for the dashboard. </p>"""
    tags_list: NotRequired["aws_sdk_cloudtrail.types.tags_list.TagsList"]
    refresh_schedule: NotRequired[
        "aws_sdk_cloudtrail.types.refresh_schedule.RefreshSchedule"
    ]
    """<p> The refresh schedule for the dashboard, if configured. </p>"""
    termination_protection_enabled: NotRequired[
        "aws_sdk_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p> Indicates whether termination protection is enabled for the dashboard. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDashboardResponse) -> dict:
    out: dict = {}
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_cloudtrail.types.dashboard_type

        out["Type"] = aws_sdk_cloudtrail.types.dashboard_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "widgets" in value:
        import aws_sdk_cloudtrail.types.widget_list

        out["Widgets"] = aws_sdk_cloudtrail.types.widget_list.serialize_aws_json_1_1(
            value["widgets"]
        )
    if "tags_list" in value:
        import aws_sdk_cloudtrail.types.tags_list

        out["TagsList"] = aws_sdk_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags_list"]
        )
    if "refresh_schedule" in value:
        import aws_sdk_cloudtrail.types.refresh_schedule

        out["RefreshSchedule"] = (
            aws_sdk_cloudtrail.types.refresh_schedule.serialize_aws_json_1_1(
                value["refresh_schedule"]
            )
        )
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDashboardResponse:
    out: CreateDashboardResponse = {}  # type: ignore[typeddict-item]
    if "DashboardArn" in data:
        out["dashboard_arn"] = data["DashboardArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_cloudtrail.types.dashboard_type

        out["type"] = aws_sdk_cloudtrail.types.dashboard_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Widgets" in data:
        import aws_sdk_cloudtrail.types.widget_list

        out["widgets"] = aws_sdk_cloudtrail.types.widget_list.deserialize_aws_json_1_1(
            data["Widgets"]
        )
    if "TagsList" in data:
        import aws_sdk_cloudtrail.types.tags_list

        out["tags_list"] = aws_sdk_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    if "RefreshSchedule" in data:
        import aws_sdk_cloudtrail.types.refresh_schedule

        out["refresh_schedule"] = (
            aws_sdk_cloudtrail.types.refresh_schedule.deserialize_aws_json_1_1(
                data["RefreshSchedule"]
            )
        )
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    return out
