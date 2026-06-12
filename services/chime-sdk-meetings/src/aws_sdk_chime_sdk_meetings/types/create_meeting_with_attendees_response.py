"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateMeetingWithAttendeesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee_list
    import aws_sdk_chime_sdk_meetings.types.batch_create_attendee_error_list
    import aws_sdk_chime_sdk_meetings.types.meeting


class CreateMeetingWithAttendeesResponse(TypedDict):
    meeting: NotRequired["aws_sdk_chime_sdk_meetings.types.meeting.Meeting"]
    """<p>The meeting information, including the meeting ID and <code>MediaPlacement</code>.</p>"""
    attendees: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.attendee_list.AttendeeList"
    ]
    """<p>The attendee information, including attendees' IDs and join tokens.</p>"""
    errors: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.batch_create_attendee_error_list.BatchCreateAttendeeErrorList"
    ]
    """<p>If the action fails for one or more of the attendees in the request, a list of the attendees is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingWithAttendeesResponse) -> dict:
    out: dict = {}
    if "meeting" in value:
        import aws_sdk_chime_sdk_meetings.types.meeting

        out["Meeting"] = aws_sdk_chime_sdk_meetings.types.meeting.serialize_json(
            value["meeting"]
        )
    if "attendees" in value:
        import aws_sdk_chime_sdk_meetings.types.attendee_list

        out["Attendees"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_list.serialize_json(
                value["attendees"]
            )
        )
    if "errors" in value:
        import aws_sdk_chime_sdk_meetings.types.batch_create_attendee_error_list

        out["Errors"] = (
            aws_sdk_chime_sdk_meetings.types.batch_create_attendee_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMeetingWithAttendeesResponse:
    out: CreateMeetingWithAttendeesResponse = {}  # type: ignore[typeddict-item]
    if "Meeting" in data:
        import aws_sdk_chime_sdk_meetings.types.meeting

        out["meeting"] = aws_sdk_chime_sdk_meetings.types.meeting.deserialize_json(
            data["Meeting"]
        )
    if "Attendees" in data:
        import aws_sdk_chime_sdk_meetings.types.attendee_list

        out["attendees"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_list.deserialize_json(
                data["Attendees"]
            )
        )
    if "Errors" in data:
        import aws_sdk_chime_sdk_meetings.types.batch_create_attendee_error_list

        out["errors"] = (
            aws_sdk_chime_sdk_meetings.types.batch_create_attendee_error_list.deserialize_json(
                data["Errors"]
            )
        )
    return out
