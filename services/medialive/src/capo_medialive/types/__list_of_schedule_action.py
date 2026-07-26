"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfScheduleAction``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.schedule_action

__listOfScheduleAction: TypeAlias = list[
    "capo_medialive.types.schedule_action.ScheduleAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfScheduleAction) -> list:
    import capo_medialive.types.schedule_action

    out: list = []
    for item in value:
        out.append(capo_medialive.types.schedule_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfScheduleAction:
    import capo_medialive.types.schedule_action

    out: __listOfScheduleAction = []
    for item in data:
        out.append(capo_medialive.types.schedule_action.deserialize_json(item))
    return out
