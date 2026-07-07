"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ScheduledReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dashboard_arn
    import aws_sdk_bcm_dashboards.types.generic_string
    import aws_sdk_bcm_dashboards.types.health_status
    import aws_sdk_bcm_dashboards.types.schedule_state
    import aws_sdk_bcm_dashboards.types.scheduled_report_arn
    import aws_sdk_bcm_dashboards.types.scheduled_report_name
    import aws_sdk_bcm_dashboards.types.widget_id_list


class ScheduledReportSummary(TypedDict, closed=True):
    arn: "aws_sdk_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    """<p>The ARN of the scheduled report.</p>"""
    name: "aws_sdk_bcm_dashboards.types.scheduled_report_name.ScheduledReportName"
    """<p>The name of the scheduled report.</p>"""
    dashboard_arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard associated with the scheduled report.</p>"""
    schedule_expression: "aws_sdk_bcm_dashboards.types.generic_string.GenericString"
    """<p>The schedule expression that defines when the report runs.</p>"""
    state: "aws_sdk_bcm_dashboards.types.schedule_state.ScheduleState"
    """<p>The state of the schedule: <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    health_status: "aws_sdk_bcm_dashboards.types.health_status.HealthStatus"
    """<p>The health status of the scheduled report as of its last refresh time.</p>"""
    schedule_expression_time_zone: NotRequired[
        "aws_sdk_bcm_dashboards.types.generic_string.GenericString"
    ]
    """<p>The time zone for the schedule expression, for example, <code>UTC</code>.</p>"""
    widget_ids: NotRequired["aws_sdk_bcm_dashboards.types.widget_id_list.WidgetIdList"]
    """<p>The list of widget identifiers included in the scheduled report.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledReportSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["dashboardArn"] = value["dashboard_arn"]
    out["scheduleExpression"] = value["schedule_expression"]
    import aws_sdk_bcm_dashboards.types.schedule_state

    out["state"] = aws_sdk_bcm_dashboards.types.schedule_state.serialize_aws_json_1_0(
        value["state"]
    )
    import aws_sdk_bcm_dashboards.types.health_status

    out["healthStatus"] = (
        aws_sdk_bcm_dashboards.types.health_status.serialize_aws_json_1_0(
            value["health_status"]
        )
    )
    if "schedule_expression_time_zone" in value:
        out["scheduleExpressionTimeZone"] = value["schedule_expression_time_zone"]
    if "widget_ids" in value:
        import aws_sdk_bcm_dashboards.types.widget_id_list

        out["widgetIds"] = (
            aws_sdk_bcm_dashboards.types.widget_id_list.serialize_aws_json_1_0(
                value["widget_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledReportSummary:
    out: ScheduledReportSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ScheduledReportSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ScheduledReportSummary.name required")
    if "dashboardArn" in data:
        out["dashboard_arn"] = data["dashboardArn"]
    else:
        raise DeserializationError("ScheduledReportSummary.dashboard_arn required")
    if "scheduleExpression" in data:
        out["schedule_expression"] = data["scheduleExpression"]
    else:
        raise DeserializationError(
            "ScheduledReportSummary.schedule_expression required"
        )
    if "state" in data:
        import aws_sdk_bcm_dashboards.types.schedule_state

        out["state"] = (
            aws_sdk_bcm_dashboards.types.schedule_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        raise DeserializationError("ScheduledReportSummary.state required")
    if "healthStatus" in data:
        import aws_sdk_bcm_dashboards.types.health_status

        out["health_status"] = (
            aws_sdk_bcm_dashboards.types.health_status.deserialize_aws_json_1_0(
                data["healthStatus"]
            )
        )
    else:
        raise DeserializationError("ScheduledReportSummary.health_status required")
    if "scheduleExpressionTimeZone" in data:
        out["schedule_expression_time_zone"] = data["scheduleExpressionTimeZone"]
    if "widgetIds" in data:
        import aws_sdk_bcm_dashboards.types.widget_id_list

        out["widget_ids"] = (
            aws_sdk_bcm_dashboards.types.widget_id_list.deserialize_aws_json_1_0(
                data["widgetIds"]
            )
        )
    return out
