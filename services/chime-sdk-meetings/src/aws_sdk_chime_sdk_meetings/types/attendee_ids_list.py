"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AttendeeIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee_id_item

AttendeeIdsList: TypeAlias = list[
    "aws_sdk_chime_sdk_meetings.types.attendee_id_item.AttendeeIdItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeIdsList) -> list:
    import aws_sdk_chime_sdk_meetings.types.attendee_id_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_meetings.types.attendee_id_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttendeeIdsList:
    import aws_sdk_chime_sdk_meetings.types.attendee_id_item

    out: AttendeeIdsList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_meetings.types.attendee_id_item.deserialize_json(item)
        )
    return out
