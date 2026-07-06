"""Generated from Smithy shape ``com.amazonaws.scheduler#ListSchedulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.next_token
    import aws_sdk_scheduler.types.schedule_list


class ListSchedulesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_scheduler.types.next_token.NextToken"]
    """<p>Indicates whether there are additional results to retrieve. If the value is null, there are no more results.</p>"""
    schedules: "aws_sdk_scheduler.types.schedule_list.ScheduleList"
    """<p>The schedules that match the specified criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchedulesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_scheduler.types.schedule_list

    out["Schedules"] = aws_sdk_scheduler.types.schedule_list.serialize_json(
        value["schedules"]
    )
    return out


def deserialize_json(data: dict) -> ListSchedulesOutput:
    out: ListSchedulesOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Schedules" in data:
        import aws_sdk_scheduler.types.schedule_list

        out["schedules"] = aws_sdk_scheduler.types.schedule_list.deserialize_json(
            data["Schedules"]
        )
    else:
        raise DeserializationError("ListSchedulesOutput.schedules required")
    return out
