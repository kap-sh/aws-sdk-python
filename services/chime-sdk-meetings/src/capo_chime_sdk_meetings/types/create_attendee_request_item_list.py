"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateAttendeeRequestItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.create_attendee_request_item

CreateAttendeeRequestItemList: TypeAlias = list[
    "capo_chime_sdk_meetings.types.create_attendee_request_item.CreateAttendeeRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttendeeRequestItemList) -> list:
    import capo_chime_sdk_meetings.types.create_attendee_request_item

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_meetings.types.create_attendee_request_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateAttendeeRequestItemList:
    import capo_chime_sdk_meetings.types.create_attendee_request_item

    out: CreateAttendeeRequestItemList = []
    for item in data:
        out.append(
            capo_chime_sdk_meetings.types.create_attendee_request_item.deserialize_json(
                item
            )
        )
    return out
