"""Generated from Smithy shape ``com.amazonaws.iot#ScheduledJobRollout``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.string_date_time


class ScheduledJobRollout(TypedDict):
    start_time: NotRequired["aws_sdk_iot.types.string_date_time.StringDateTime"]
    """<p>Displays the start times of the next seven maintenance window occurrences.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledJobRollout) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    return out


def deserialize_json(data: dict) -> ScheduledJobRollout:
    out: ScheduledJobRollout = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    return out
