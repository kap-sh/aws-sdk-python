"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AttendeeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee

AttendeeList: TypeAlias = list["aws_sdk_chime_sdk_meetings.types.attendee.Attendee"]


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeList) -> list:
    import aws_sdk_chime_sdk_meetings.types.attendee

    out: list = []
    for item in value:
        out.append(aws_sdk_chime_sdk_meetings.types.attendee.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttendeeList:
    import aws_sdk_chime_sdk_meetings.types.attendee

    out: AttendeeList = []
    for item in data:
        out.append(aws_sdk_chime_sdk_meetings.types.attendee.deserialize_json(item))
    return out
