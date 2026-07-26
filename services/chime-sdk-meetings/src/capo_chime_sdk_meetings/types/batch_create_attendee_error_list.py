"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#BatchCreateAttendeeErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.create_attendee_error

BatchCreateAttendeeErrorList: TypeAlias = list[
    "capo_chime_sdk_meetings.types.create_attendee_error.CreateAttendeeError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateAttendeeErrorList) -> list:
    import capo_chime_sdk_meetings.types.create_attendee_error

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_meetings.types.create_attendee_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchCreateAttendeeErrorList:
    import capo_chime_sdk_meetings.types.create_attendee_error

    out: BatchCreateAttendeeErrorList = []
    for item in data:
        out.append(
            capo_chime_sdk_meetings.types.create_attendee_error.deserialize_json(item)
        )
    return out
