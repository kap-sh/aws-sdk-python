"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingPlanForUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.integer
    import capo_backup.types.restore_testing_recovery_point_selection


class RestoreTestingPlanForUpdate(TypedDict, closed=True):
    recovery_point_selection: NotRequired[
        "capo_backup.types.restore_testing_recovery_point_selection.RestoreTestingRecoveryPointSelection"
    ]
    """<p>Required: <code>Algorithm</code>; <code>RecoveryPointTypes</code>; <code>IncludeVaults</code> (<i>one or more</i>).</p> <p>Optional: <i>SelectionWindowDays</i> (<i>'30' if not specified</i>); <code>ExcludeVaults</code> (defaults to empty list if not listed).</p>"""
    schedule_expression: NotRequired["str"]
    """<p>A CRON expression in specified timezone when a restore testing plan is executed. When no CRON expression is provided, Backup will use the default expression <code>cron(0 5 ? * * *)</code>.</p>"""
    schedule_expression_timezone: NotRequired["str"]
    """<p>Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.</p>"""
    start_window_hours: "capo_backup.types.integer.integer"
    """<p>Defaults to 24 hours.</p> <p>A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingPlanForUpdate) -> dict:
    out: dict = {}
    if "recovery_point_selection" in value:
        import capo_backup.types.restore_testing_recovery_point_selection

        out["RecoveryPointSelection"] = (
            capo_backup.types.restore_testing_recovery_point_selection.serialize_json(
                value["recovery_point_selection"]
            )
        )
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "schedule_expression_timezone" in value:
        out["ScheduleExpressionTimezone"] = value["schedule_expression_timezone"]
    out["StartWindowHours"] = value.get("start_window_hours", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingPlanForUpdate:
    out: RestoreTestingPlanForUpdate = {}  # type: ignore[typeddict-item]
    if "RecoveryPointSelection" in data:
        import capo_backup.types.restore_testing_recovery_point_selection

        out["recovery_point_selection"] = (
            capo_backup.types.restore_testing_recovery_point_selection.deserialize_json(
                data["RecoveryPointSelection"]
            )
        )
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    if "ScheduleExpressionTimezone" in data:
        out["schedule_expression_timezone"] = data["ScheduleExpressionTimezone"]
    if "StartWindowHours" in data:
        out["start_window_hours"] = data["StartWindowHours"]
    else:
        out["start_window_hours"] = 0
    return out
