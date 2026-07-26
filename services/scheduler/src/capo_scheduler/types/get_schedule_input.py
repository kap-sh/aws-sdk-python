"""Generated from Smithy shape ``com.amazonaws.scheduler#GetScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.name
    import capo_scheduler.types.schedule_group_name


class GetScheduleInput(TypedDict, closed=True):
    name: "capo_scheduler.types.name.Name"
    """<p>The name of the schedule to retrieve.</p>"""
    group_name: NotRequired[
        "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
    ]
    """<p>The name of the schedule group associated with this schedule. If you omit this, EventBridge Scheduler assumes that the schedule is associated with the default group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScheduleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetScheduleInput:
    out: GetScheduleInput = {}  # type: ignore[typeddict-item]
    return out
