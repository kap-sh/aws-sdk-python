"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#BatchCreateAttendeeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list
    import aws_sdk_chime_sdk_meetings.types.guid_string


class BatchCreateAttendeeRequest(TypedDict):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK ID of the meeting to which you're adding attendees.</p>"""
    attendees: "aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list.CreateAttendeeRequestItemList"
    """<p>The attendee information, including attendees' IDs and join tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateAttendeeRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list

    out["Attendees"] = (
        aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list.serialize_json(
            value["attendees"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateAttendeeRequest:
    out: BatchCreateAttendeeRequest = {}  # type: ignore[typeddict-item]
    if "Attendees" in data:
        import aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list

        out["attendees"] = (
            aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list.deserialize_json(
                data["Attendees"]
            )
        )
    else:
        raise DeserializationError("BatchCreateAttendeeRequest.attendees required")
    return out
