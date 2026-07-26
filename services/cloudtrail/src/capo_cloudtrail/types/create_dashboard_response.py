"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_arn
    import capo_cloudtrail.types.dashboard_name
    import capo_cloudtrail.types.dashboard_type
    import capo_cloudtrail.types.refresh_schedule
    import capo_cloudtrail.types.tags_list
    import capo_cloudtrail.types.termination_protection_enabled
    import capo_cloudtrail.types.widget_list


class CreateDashboardResponse(TypedDict, closed=True):
    dashboard_arn: NotRequired["capo_cloudtrail.types.dashboard_arn.DashboardArn"]
    """<p> The ARN for the dashboard. </p>"""
    name: NotRequired["capo_cloudtrail.types.dashboard_name.DashboardName"]
    """<p> The name of the dashboard. </p>"""
    type: NotRequired["capo_cloudtrail.types.dashboard_type.DashboardType"]
    """<p> The dashboard type. </p>"""
    widgets: NotRequired["capo_cloudtrail.types.widget_list.WidgetList"]
    """<p> An array of widgets for the dashboard. </p>"""
    tags_list: NotRequired["capo_cloudtrail.types.tags_list.TagsList"]
    refresh_schedule: NotRequired[
        "capo_cloudtrail.types.refresh_schedule.RefreshSchedule"
    ]
    """<p> The refresh schedule for the dashboard, if configured. </p>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
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
        import capo_cloudtrail.types.dashboard_type

        out["Type"] = capo_cloudtrail.types.dashboard_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "widgets" in value:
        import capo_cloudtrail.types.widget_list

        out["Widgets"] = capo_cloudtrail.types.widget_list.serialize_aws_json_1_1(
            value["widgets"]
        )
    if "tags_list" in value:
        import capo_cloudtrail.types.tags_list

        out["TagsList"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags_list"]
        )
    if "refresh_schedule" in value:
        import capo_cloudtrail.types.refresh_schedule

        out["RefreshSchedule"] = (
            capo_cloudtrail.types.refresh_schedule.serialize_aws_json_1_1(
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
        import capo_cloudtrail.types.dashboard_type

        out["type"] = capo_cloudtrail.types.dashboard_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Widgets" in data:
        import capo_cloudtrail.types.widget_list

        out["widgets"] = capo_cloudtrail.types.widget_list.deserialize_aws_json_1_1(
            data["Widgets"]
        )
    if "TagsList" in data:
        import capo_cloudtrail.types.tags_list

        out["tags_list"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    if "RefreshSchedule" in data:
        import capo_cloudtrail.types.refresh_schedule

        out["refresh_schedule"] = (
            capo_cloudtrail.types.refresh_schedule.deserialize_aws_json_1_1(
                data["RefreshSchedule"]
            )
        )
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    return out
