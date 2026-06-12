"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdatePracticeRunConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.allowed_windows
    import aws_sdk_arc_zonal_shift.types.blocked_dates
    import aws_sdk_arc_zonal_shift.types.blocked_windows
    import aws_sdk_arc_zonal_shift.types.blocking_alarms
    import aws_sdk_arc_zonal_shift.types.outcome_alarms
    import aws_sdk_arc_zonal_shift.types.resource_identifier


class UpdatePracticeRunConfigurationRequest(TypedDict):
    resource_identifier: (
        "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that you want to update the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""
    blocked_windows: NotRequired[
        "aws_sdk_arc_zonal_shift.types.blocked_windows.BlockedWindows"
    ]
    """<p>Add, change, or remove windows of days and times for when you can, optionally, block ARC from starting a practice run for a resource.</p> <p>The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.</p> <p>For example, say you run business report summaries three days a week. For this scenario, you might set the following recurring days and times as blocked windows, for example: <code>MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30</code>.</p>"""
    blocked_dates: NotRequired[
        "aws_sdk_arc_zonal_shift.types.blocked_dates.BlockedDates"
    ]
    """<p>Add, change, or remove blocked dates for a practice run in zonal autoshift.</p> <p>Optionally, you can block practice runs for specific calendar dates. The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.</p> <p>For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for <code>2024-05-01</code>.</p>"""
    blocking_alarms: NotRequired[
        "aws_sdk_arc_zonal_shift.types.blocking_alarms.BlockingAlarms"
    ]
    """<p>Add, change, or remove the Amazon CloudWatch alarms that you optionally specify as the blocking alarms for practice runs.</p>"""
    allowed_windows: NotRequired[
        "aws_sdk_arc_zonal_shift.types.allowed_windows.AllowedWindows"
    ]
    """<p>Add, change, or remove windows of days and times for when you can, optionally, allow ARC to start a practice run for a resource.</p> <p>The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.</p> <p>For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: <code>Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00</code>.</p> <important> <p>The <code>allowedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>"""
    outcome_alarms: NotRequired[
        "aws_sdk_arc_zonal_shift.types.outcome_alarms.OutcomeAlarms"
    ]
    """<p>Specify one or more Amazon CloudWatch alarms as the outcome alarms for practice runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePracticeRunConfigurationRequest) -> dict:
    out: dict = {}
    if "blocked_windows" in value:
        import aws_sdk_arc_zonal_shift.types.blocked_windows

        out["blockedWindows"] = (
            aws_sdk_arc_zonal_shift.types.blocked_windows.serialize_json(
                value["blocked_windows"]
            )
        )
    if "blocked_dates" in value:
        import aws_sdk_arc_zonal_shift.types.blocked_dates

        out["blockedDates"] = (
            aws_sdk_arc_zonal_shift.types.blocked_dates.serialize_json(
                value["blocked_dates"]
            )
        )
    if "blocking_alarms" in value:
        import aws_sdk_arc_zonal_shift.types.blocking_alarms

        out["blockingAlarms"] = (
            aws_sdk_arc_zonal_shift.types.blocking_alarms.serialize_json(
                value["blocking_alarms"]
            )
        )
    if "allowed_windows" in value:
        import aws_sdk_arc_zonal_shift.types.allowed_windows

        out["allowedWindows"] = (
            aws_sdk_arc_zonal_shift.types.allowed_windows.serialize_json(
                value["allowed_windows"]
            )
        )
    if "outcome_alarms" in value:
        import aws_sdk_arc_zonal_shift.types.outcome_alarms

        out["outcomeAlarms"] = (
            aws_sdk_arc_zonal_shift.types.outcome_alarms.serialize_json(
                value["outcome_alarms"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePracticeRunConfigurationRequest:
    out: UpdatePracticeRunConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "blockedWindows" in data:
        import aws_sdk_arc_zonal_shift.types.blocked_windows

        out["blocked_windows"] = (
            aws_sdk_arc_zonal_shift.types.blocked_windows.deserialize_json(
                data["blockedWindows"]
            )
        )
    if "blockedDates" in data:
        import aws_sdk_arc_zonal_shift.types.blocked_dates

        out["blocked_dates"] = (
            aws_sdk_arc_zonal_shift.types.blocked_dates.deserialize_json(
                data["blockedDates"]
            )
        )
    if "blockingAlarms" in data:
        import aws_sdk_arc_zonal_shift.types.blocking_alarms

        out["blocking_alarms"] = (
            aws_sdk_arc_zonal_shift.types.blocking_alarms.deserialize_json(
                data["blockingAlarms"]
            )
        )
    if "allowedWindows" in data:
        import aws_sdk_arc_zonal_shift.types.allowed_windows

        out["allowed_windows"] = (
            aws_sdk_arc_zonal_shift.types.allowed_windows.deserialize_json(
                data["allowedWindows"]
            )
        )
    if "outcomeAlarms" in data:
        import aws_sdk_arc_zonal_shift.types.outcome_alarms

        out["outcome_alarms"] = (
            aws_sdk_arc_zonal_shift.types.outcome_alarms.deserialize_json(
                data["outcomeAlarms"]
            )
        )
    return out
