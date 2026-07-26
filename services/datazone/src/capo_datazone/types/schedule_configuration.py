"""Generated from Smithy shape ``com.amazonaws.datazone#ScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.cron_string
    import capo_datazone.types.timezone


class ScheduleConfiguration(TypedDict, closed=True):
    timezone: NotRequired["capo_datazone.types.timezone.Timezone"]
    """<p>The timezone of the data source run. </p>"""
    schedule: NotRequired["capo_datazone.types.cron_string.CronString"]
    """<p>The schedule of the data source runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    if "timezone" in value:
        import capo_datazone.types.timezone

        out["timezone"] = capo_datazone.types.timezone.serialize_json(value["timezone"])
    if "schedule" in value:
        out["schedule"] = value["schedule"]
    return out


def deserialize_json(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "timezone" in data:
        import capo_datazone.types.timezone

        out["timezone"] = capo_datazone.types.timezone.deserialize_json(
            data["timezone"]
        )
    if "schedule" in data:
        out["schedule"] = data["schedule"]
    return out
