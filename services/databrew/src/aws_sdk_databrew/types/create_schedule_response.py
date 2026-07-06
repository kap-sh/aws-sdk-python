"""Generated from Smithy shape ``com.amazonaws.databrew#CreateScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.schedule_name


class CreateScheduleResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateScheduleResponse:
    out: CreateScheduleResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateScheduleResponse.name required")
    return out
