"""Generated from Smithy shape ``com.amazonaws.scheduler#CreateScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.schedule_arn


class CreateScheduleOutput(TypedDict, closed=True):
    schedule_arn: "aws_sdk_scheduler.types.schedule_arn.ScheduleArn"
    """<p>The Amazon Resource Name (ARN) of the schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleOutput) -> dict:
    out: dict = {}
    out["ScheduleArn"] = value["schedule_arn"]
    return out


def deserialize_json(data: dict) -> CreateScheduleOutput:
    out: CreateScheduleOutput = {}  # type: ignore[typeddict-item]
    if "ScheduleArn" in data:
        out["schedule_arn"] = data["ScheduleArn"]
    else:
        raise DeserializationError("CreateScheduleOutput.schedule_arn required")
    return out
