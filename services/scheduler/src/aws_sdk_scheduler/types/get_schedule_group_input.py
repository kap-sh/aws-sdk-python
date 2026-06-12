"""Generated from Smithy shape ``com.amazonaws.scheduler#GetScheduleGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.schedule_group_name


class GetScheduleGroupInput(TypedDict):
    name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName"
    """<p>The name of the schedule group to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScheduleGroupInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetScheduleGroupInput:
    out: GetScheduleGroupInput = {}  # type: ignore[typeddict-item]
    return out
