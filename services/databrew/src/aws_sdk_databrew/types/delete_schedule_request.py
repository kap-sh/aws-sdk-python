"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.schedule_name


class DeleteScheduleRequest(TypedDict):
    name: "aws_sdk_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduleRequest:
    out: DeleteScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
