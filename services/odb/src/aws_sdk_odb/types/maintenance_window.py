"""Generated from Smithy shape ``com.amazonaws.odb#MaintenanceWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.days_of_week
    import aws_sdk_odb.types.hours_of_day
    import aws_sdk_odb.types.months
    import aws_sdk_odb.types.patching_mode_type
    import aws_sdk_odb.types.preference_type
    import aws_sdk_odb.types.weeks_of_month


class MaintenanceWindow(TypedDict, closed=True):
    custom_action_timeout_in_mins: NotRequired["int"]
    """<p>The custom action timeout in minutes for the maintenance window.</p>"""
    days_of_week: NotRequired["aws_sdk_odb.types.days_of_week.DaysOfWeek"]
    """<p>The days of the week when maintenance can be performed.</p>"""
    hours_of_day: NotRequired["aws_sdk_odb.types.hours_of_day.HoursOfDay"]
    """<p>The hours of the day when maintenance can be performed.</p>"""
    is_custom_action_timeout_enabled: NotRequired["bool"]
    """<p>Indicates whether custom action timeout is enabled for the maintenance window.</p>"""
    lead_time_in_weeks: NotRequired["int"]
    """<p>The lead time in weeks before the maintenance window.</p>"""
    months: NotRequired["aws_sdk_odb.types.months.Months"]
    """<p>The months when maintenance can be performed.</p>"""
    patching_mode: NotRequired["aws_sdk_odb.types.patching_mode_type.PatchingModeType"]
    """<p>The patching mode for the maintenance window.</p>"""
    preference: NotRequired["aws_sdk_odb.types.preference_type.PreferenceType"]
    """<p>The preference for the maintenance window scheduling.</p>"""
    skip_ru: NotRequired["bool"]
    """<p>Indicates whether to skip release updates during maintenance.</p>"""
    weeks_of_month: NotRequired["aws_sdk_odb.types.weeks_of_month.WeeksOfMonth"]
    """<p>The weeks of the month when maintenance can be performed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MaintenanceWindow) -> dict:
    out: dict = {}
    if "custom_action_timeout_in_mins" in value:
        out["customActionTimeoutInMins"] = value["custom_action_timeout_in_mins"]
    if "days_of_week" in value:
        import aws_sdk_odb.types.days_of_week

        out["daysOfWeek"] = aws_sdk_odb.types.days_of_week.serialize_aws_json_1_0(
            value["days_of_week"]
        )
    if "hours_of_day" in value:
        import aws_sdk_odb.types.hours_of_day

        out["hoursOfDay"] = aws_sdk_odb.types.hours_of_day.serialize_aws_json_1_0(
            value["hours_of_day"]
        )
    if "is_custom_action_timeout_enabled" in value:
        out["isCustomActionTimeoutEnabled"] = value["is_custom_action_timeout_enabled"]
    if "lead_time_in_weeks" in value:
        out["leadTimeInWeeks"] = value["lead_time_in_weeks"]
    if "months" in value:
        import aws_sdk_odb.types.months

        out["months"] = aws_sdk_odb.types.months.serialize_aws_json_1_0(value["months"])
    if "patching_mode" in value:
        import aws_sdk_odb.types.patching_mode_type

        out["patchingMode"] = (
            aws_sdk_odb.types.patching_mode_type.serialize_aws_json_1_0(
                value["patching_mode"]
            )
        )
    if "preference" in value:
        import aws_sdk_odb.types.preference_type

        out["preference"] = aws_sdk_odb.types.preference_type.serialize_aws_json_1_0(
            value["preference"]
        )
    if "skip_ru" in value:
        out["skipRu"] = value["skip_ru"]
    if "weeks_of_month" in value:
        import aws_sdk_odb.types.weeks_of_month

        out["weeksOfMonth"] = aws_sdk_odb.types.weeks_of_month.serialize_aws_json_1_0(
            value["weeks_of_month"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MaintenanceWindow:
    out: MaintenanceWindow = {}  # type: ignore[typeddict-item]
    if "customActionTimeoutInMins" in data:
        out["custom_action_timeout_in_mins"] = data["customActionTimeoutInMins"]
    if "daysOfWeek" in data:
        import aws_sdk_odb.types.days_of_week

        out["days_of_week"] = aws_sdk_odb.types.days_of_week.deserialize_aws_json_1_0(
            data["daysOfWeek"]
        )
    if "hoursOfDay" in data:
        import aws_sdk_odb.types.hours_of_day

        out["hours_of_day"] = aws_sdk_odb.types.hours_of_day.deserialize_aws_json_1_0(
            data["hoursOfDay"]
        )
    if "isCustomActionTimeoutEnabled" in data:
        out["is_custom_action_timeout_enabled"] = data["isCustomActionTimeoutEnabled"]
    if "leadTimeInWeeks" in data:
        out["lead_time_in_weeks"] = data["leadTimeInWeeks"]
    if "months" in data:
        import aws_sdk_odb.types.months

        out["months"] = aws_sdk_odb.types.months.deserialize_aws_json_1_0(
            data["months"]
        )
    if "patchingMode" in data:
        import aws_sdk_odb.types.patching_mode_type

        out["patching_mode"] = (
            aws_sdk_odb.types.patching_mode_type.deserialize_aws_json_1_0(
                data["patchingMode"]
            )
        )
    if "preference" in data:
        import aws_sdk_odb.types.preference_type

        out["preference"] = aws_sdk_odb.types.preference_type.deserialize_aws_json_1_0(
            data["preference"]
        )
    if "skipRu" in data:
        out["skip_ru"] = data["skipRu"]
    if "weeksOfMonth" in data:
        import aws_sdk_odb.types.weeks_of_month

        out["weeks_of_month"] = (
            aws_sdk_odb.types.weeks_of_month.deserialize_aws_json_1_0(
                data["weeksOfMonth"]
            )
        )
    return out
