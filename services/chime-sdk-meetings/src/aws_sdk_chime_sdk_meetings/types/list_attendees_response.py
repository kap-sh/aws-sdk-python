"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ListAttendeesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee_list
    import aws_sdk_chime_sdk_meetings.types.string


class ListAttendeesResponse(TypedDict):
    attendees: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.attendee_list.AttendeeList"
    ]
    """<p>The Amazon Chime SDK attendee information.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttendeesResponse) -> dict:
    out: dict = {}
    if "attendees" in value:
        import aws_sdk_chime_sdk_meetings.types.attendee_list

        out["Attendees"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_list.serialize_json(
                value["attendees"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttendeesResponse:
    out: ListAttendeesResponse = {}  # type: ignore[typeddict-item]
    if "Attendees" in data:
        import aws_sdk_chime_sdk_meetings.types.attendee_list

        out["attendees"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_list.deserialize_json(
                data["Attendees"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
