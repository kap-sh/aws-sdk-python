"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ScheduleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.generic_string
    import capo_bcm_dashboards.types.schedule_period
    import capo_bcm_dashboards.types.schedule_state


class ScheduleConfig(TypedDict, closed=True):
    schedule_expression: NotRequired[
        "capo_bcm_dashboards.types.generic_string.GenericString"
    ]
    """<p>The schedule expression that specifies when to trigger the scheduled report run. This value must be a cron expression consisting of six fields separated by white spaces: <code>cron(minutes hours day_of_month month day_of_week year)</code>.</p>"""
    schedule_expression_time_zone: NotRequired[
        "capo_bcm_dashboards.types.generic_string.GenericString"
    ]
    """<p>The time zone for the schedule expression, for example, <code>UTC</code>.</p>"""
    schedule_period: NotRequired[
        "capo_bcm_dashboards.types.schedule_period.SchedulePeriod"
    ]
    """<p>The time period during which the schedule is active.</p>"""
    state: NotRequired["capo_bcm_dashboards.types.schedule_state.ScheduleState"]
    """<p>The state of the schedule. <code>ENABLED</code> means the scheduled report runs according to its schedule expression. <code>DISABLED</code> means the scheduled report is paused and will not run until re-enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleConfig) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["scheduleExpression"] = value["schedule_expression"]
    if "schedule_expression_time_zone" in value:
        out["scheduleExpressionTimeZone"] = value["schedule_expression_time_zone"]
    if "schedule_period" in value:
        import capo_bcm_dashboards.types.schedule_period

        out["schedulePeriod"] = (
            capo_bcm_dashboards.types.schedule_period.serialize_aws_json_1_0(
                value["schedule_period"]
            )
        )
    if "state" in value:
        import capo_bcm_dashboards.types.schedule_state

        out["state"] = capo_bcm_dashboards.types.schedule_state.serialize_aws_json_1_0(
            value["state"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleConfig:
    out: ScheduleConfig = {}  # type: ignore[typeddict-item]
    if "scheduleExpression" in data:
        out["schedule_expression"] = data["scheduleExpression"]
    if "scheduleExpressionTimeZone" in data:
        out["schedule_expression_time_zone"] = data["scheduleExpressionTimeZone"]
    if "schedulePeriod" in data:
        import capo_bcm_dashboards.types.schedule_period

        out["schedule_period"] = (
            capo_bcm_dashboards.types.schedule_period.deserialize_aws_json_1_0(
                data["schedulePeriod"]
            )
        )
    if "state" in data:
        import capo_bcm_dashboards.types.schedule_state

        out["state"] = (
            capo_bcm_dashboards.types.schedule_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    return out
