"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.schedule_name


class DescribeScheduleRequest(TypedDict):
    name: "aws_sdk_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeScheduleRequest:
    out: DescribeScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
