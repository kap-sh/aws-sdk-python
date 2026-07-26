"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_arn
    import capo_cloudtrail.types.dashboard_status
    import capo_cloudtrail.types.dashboard_type
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.error_message
    import capo_cloudtrail.types.refresh_id
    import capo_cloudtrail.types.refresh_schedule
    import capo_cloudtrail.types.termination_protection_enabled
    import capo_cloudtrail.types.widget_list


class GetDashboardResponse(TypedDict, closed=True):
    dashboard_arn: NotRequired["capo_cloudtrail.types.dashboard_arn.DashboardArn"]
    """<p> The ARN for the dashboard. </p>"""
    type: NotRequired["capo_cloudtrail.types.dashboard_type.DashboardType"]
    """<p> The type of dashboard. </p>"""
    status: NotRequired["capo_cloudtrail.types.dashboard_status.DashboardStatus"]
    """<p> The status of the dashboard. </p>"""
    widgets: NotRequired["capo_cloudtrail.types.widget_list.WidgetList"]
    """<p> An array of widgets for the dashboard. </p>"""
    refresh_schedule: NotRequired[
        "capo_cloudtrail.types.refresh_schedule.RefreshSchedule"
    ]
    """<p> The refresh schedule for the dashboard, if configured. </p>"""
    created_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> The timestamp that shows when the dashboard was created. </p>"""
    updated_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> The timestamp that shows when the dashboard was last updated. </p>"""
    last_refresh_id: NotRequired["capo_cloudtrail.types.refresh_id.RefreshId"]
    """<p> The ID of the last dashboard refresh. </p>"""
    last_refresh_failure_reason: NotRequired[
        "capo_cloudtrail.types.error_message.ErrorMessage"
    ]
    """<p> Provides information about failures for the last scheduled refresh. </p>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p> Indicates whether termination protection is enabled for the dashboard. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDashboardResponse) -> dict:
    out: dict = {}
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "type" in value:
        import capo_cloudtrail.types.dashboard_type

        out["Type"] = capo_cloudtrail.types.dashboard_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_cloudtrail.types.dashboard_status

        out["Status"] = capo_cloudtrail.types.dashboard_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "widgets" in value:
        import capo_cloudtrail.types.widget_list

        out["Widgets"] = capo_cloudtrail.types.widget_list.serialize_aws_json_1_1(
            value["widgets"]
        )
    if "refresh_schedule" in value:
        import capo_cloudtrail.types.refresh_schedule

        out["RefreshSchedule"] = (
            capo_cloudtrail.types.refresh_schedule.serialize_aws_json_1_1(
                value["refresh_schedule"]
            )
        )
    if "created_timestamp" in value:
        import capo_cloudtrail.types.date

        out["CreatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_cloudtrail.types.date

        out["UpdatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["updated_timestamp"]
        )
    if "last_refresh_id" in value:
        out["LastRefreshId"] = value["last_refresh_id"]
    if "last_refresh_failure_reason" in value:
        out["LastRefreshFailureReason"] = value["last_refresh_failure_reason"]
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDashboardResponse:
    out: GetDashboardResponse = {}  # type: ignore[typeddict-item]
    if "DashboardArn" in data:
        out["dashboard_arn"] = data["DashboardArn"]
    if "Type" in data:
        import capo_cloudtrail.types.dashboard_type

        out["type"] = capo_cloudtrail.types.dashboard_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Status" in data:
        import capo_cloudtrail.types.dashboard_status

        out["status"] = capo_cloudtrail.types.dashboard_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Widgets" in data:
        import capo_cloudtrail.types.widget_list

        out["widgets"] = capo_cloudtrail.types.widget_list.deserialize_aws_json_1_1(
            data["Widgets"]
        )
    if "RefreshSchedule" in data:
        import capo_cloudtrail.types.refresh_schedule

        out["refresh_schedule"] = (
            capo_cloudtrail.types.refresh_schedule.deserialize_aws_json_1_1(
                data["RefreshSchedule"]
            )
        )
    if "CreatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["created_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["CreatedTimestamp"]
        )
    if "UpdatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["updated_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["UpdatedTimestamp"]
        )
    if "LastRefreshId" in data:
        out["last_refresh_id"] = data["LastRefreshId"]
    if "LastRefreshFailureReason" in data:
        out["last_refresh_failure_reason"] = data["LastRefreshFailureReason"]
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    return out
