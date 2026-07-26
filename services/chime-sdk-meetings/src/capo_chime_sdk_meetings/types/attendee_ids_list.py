"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AttendeeIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_id_item

AttendeeIdsList: TypeAlias = list[
    "capo_chime_sdk_meetings.types.attendee_id_item.AttendeeIdItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeIdsList) -> list:
    import capo_chime_sdk_meetings.types.attendee_id_item

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_meetings.types.attendee_id_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttendeeIdsList:
    import capo_chime_sdk_meetings.types.attendee_id_item

    out: AttendeeIdsList = []
    for item in data:
        out.append(
            capo_chime_sdk_meetings.types.attendee_id_item.deserialize_json(item)
        )
    return out
