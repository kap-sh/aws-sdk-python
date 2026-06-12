"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateDashboardResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.dashboard_arn
    import aws_sdk_cloudtrail.types.dashboard_name
    import aws_sdk_cloudtrail.types.dashboard_type
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.refresh_schedule
    import aws_sdk_cloudtrail.types.termination_protection_enabled
    import aws_sdk_cloudtrail.types.widget_list


class UpdateDashboardResponse(TypedDict):
    dashboard_arn: NotRequired["aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn"]
    """<p> The ARN for the dashboard. </p>"""
    name: NotRequired["aws_sdk_cloudtrail.types.dashboard_name.DashboardName"]
    """<p> The name for the dashboard. </p>"""
    type: NotRequired["aws_sdk_cloudtrail.types.dashboard_type.DashboardType"]
    """<p> The type of dashboard. </p>"""
    widgets: NotRequired["aws_sdk_cloudtrail.types.widget_list.WidgetList"]
    """<p> An array of widgets for the dashboard. </p>"""
    refresh_schedule: NotRequired[
        "aws_sdk_cloudtrail.types.refresh_schedule.RefreshSchedule"
    ]
    """<p> The refresh schedule for the dashboard, if configured. </p>"""
    termination_protection_enabled: NotRequired[
        "aws_sdk_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p> Indicates whether termination protection is enabled for the dashboard. </p>"""
    created_timestamp: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> The timestamp that shows when the dashboard was created. </p>"""
    updated_timestamp: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> The timestamp that shows when the dashboard was updated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDashboardResponse) -> dict:
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
    if "refresh_schedule" in value:
        import aws_sdk_cloudtrail.types.refresh_schedule

        out["RefreshSchedule"] = (
            aws_sdk_cloudtrail.types.refresh_schedule.serialize_aws_json_1_1(
                value["refresh_schedule"]
            )
        )
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
    if "created_timestamp" in value:
        import aws_sdk_cloudtrail.types.date

        out["CreatedTimestamp"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import aws_sdk_cloudtrail.types.date

        out["UpdatedTimestamp"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["updated_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDashboardResponse:
    out: UpdateDashboardResponse = {}  # type: ignore[typeddict-item]
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
    if "RefreshSchedule" in data:
        import aws_sdk_cloudtrail.types.refresh_schedule

        out["refresh_schedule"] = (
            aws_sdk_cloudtrail.types.refresh_schedule.deserialize_aws_json_1_1(
                data["RefreshSchedule"]
            )
        )
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    if "CreatedTimestamp" in data:
        import aws_sdk_cloudtrail.types.date

        out["created_timestamp"] = (
            aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_cloudtrail.types.date

        out["updated_timestamp"] = (
            aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["UpdatedTimestamp"]
            )
        )
    return out
