"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.schedule_name


class DeleteScheduleRequest(TypedDict, closed=True):
    name: "capo_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduleRequest:
    out: DeleteScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
