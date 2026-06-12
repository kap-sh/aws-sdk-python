"""Generated from Smithy shape ``com.amazonaws.scheduler#GetScheduleInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.name
    import aws_sdk_scheduler.types.schedule_group_name


class GetScheduleInput(TypedDict):
    name: "aws_sdk_scheduler.types.name.Name"
    """<p>The name of the schedule to retrieve.</p>"""
    group_name: NotRequired[
        "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName"
    ]
    """<p>The name of the schedule group associated with this schedule. If you omit this, EventBridge Scheduler assumes that the schedule is associated with the default group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScheduleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetScheduleInput:
    out: GetScheduleInput = {}  # type: ignore[typeddict-item]
    return out
