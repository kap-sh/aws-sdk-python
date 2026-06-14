"""Generated from Smithy shape ``com.amazonaws.datazone#ScheduleConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.cron_string
    import aws_sdk_datazone.types.timezone


class ScheduleConfiguration(TypedDict):
    timezone: NotRequired["aws_sdk_datazone.types.timezone.Timezone"]
    """<p>The timezone of the data source run. </p>"""
    schedule: NotRequired["aws_sdk_datazone.types.cron_string.CronString"]
    """<p>The schedule of the data source runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    if "timezone" in value:
        import aws_sdk_datazone.types.timezone

        out["timezone"] = aws_sdk_datazone.types.timezone.serialize_json(
            value["timezone"]
        )
    if "schedule" in value:
        out["schedule"] = value["schedule"]
    return out


def deserialize_json(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "timezone" in data:
        import aws_sdk_datazone.types.timezone

        out["timezone"] = aws_sdk_datazone.types.timezone.deserialize_json(
            data["timezone"]
        )
    if "schedule" in data:
        out["schedule"] = data["schedule"]
    return out
