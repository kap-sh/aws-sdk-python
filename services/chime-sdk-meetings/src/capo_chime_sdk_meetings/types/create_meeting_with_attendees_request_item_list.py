"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateMeetingWithAttendeesRequestItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.create_attendee_request_item

CreateMeetingWithAttendeesRequestItemList: TypeAlias = list[
    "capo_chime_sdk_meetings.types.create_attendee_request_item.CreateAttendeeRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingWithAttendeesRequestItemList) -> list:
    import capo_chime_sdk_meetings.types.create_attendee_request_item

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_meetings.types.create_attendee_request_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateMeetingWithAttendeesRequestItemList:
    import capo_chime_sdk_meetings.types.create_attendee_request_item

    out: CreateMeetingWithAttendeesRequestItemList = []
    for item in data:
        out.append(
            capo_chime_sdk_meetings.types.create_attendee_request_item.deserialize_json(
                item
            )
        )
    return out
