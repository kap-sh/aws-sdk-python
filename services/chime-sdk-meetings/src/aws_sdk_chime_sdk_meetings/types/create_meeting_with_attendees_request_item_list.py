"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateMeetingWithAttendeesRequestItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.create_attendee_request_item

CreateMeetingWithAttendeesRequestItemList: TypeAlias = list[
    "aws_sdk_chime_sdk_meetings.types.create_attendee_request_item.CreateAttendeeRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingWithAttendeesRequestItemList) -> list:
    import aws_sdk_chime_sdk_meetings.types.create_attendee_request_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_meetings.types.create_attendee_request_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateMeetingWithAttendeesRequestItemList:
    import aws_sdk_chime_sdk_meetings.types.create_attendee_request_item

    out: CreateMeetingWithAttendeesRequestItemList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_meetings.types.create_attendee_request_item.deserialize_json(
                item
            )
        )
    return out
