"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfScheduleEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.schedule_entry

__listOfScheduleEntry: TypeAlias = list[
    "capo_mediatailor.types.schedule_entry.ScheduleEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfScheduleEntry) -> list:
    import capo_mediatailor.types.schedule_entry

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.schedule_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfScheduleEntry:
    import capo_mediatailor.types.schedule_entry

    out: __listOfScheduleEntry = []
    for item in data:
        out.append(capo_mediatailor.types.schedule_entry.deserialize_json(item))
    return out
