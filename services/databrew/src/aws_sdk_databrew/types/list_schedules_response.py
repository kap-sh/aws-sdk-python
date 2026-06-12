"""Generated from Smithy shape ``com.amazonaws.databrew#ListSchedulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.next_token
    import aws_sdk_databrew.types.schedule_list


class ListSchedulesResponse(TypedDict):
    schedules: "aws_sdk_databrew.types.schedule_list.ScheduleList"
    """<p>A list of schedules that are defined.</p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchedulesResponse) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.schedule_list

    out["Schedules"] = aws_sdk_databrew.types.schedule_list.serialize_json(
        value["schedules"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchedulesResponse:
    out: ListSchedulesResponse = {}  # type: ignore[typeddict-item]
    if "Schedules" in data:
        import aws_sdk_databrew.types.schedule_list

        out["schedules"] = aws_sdk_databrew.types.schedule_list.deserialize_json(
            data["Schedules"]
        )
    else:
        raise DeserializationError("ListSchedulesResponse.schedules required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
