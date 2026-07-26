"""Generated from Smithy shape ``com.amazonaws.inspector2#DaysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.day

DaysList: TypeAlias = list["capo_inspector2.types.day.Day"]


# --- restJson1 ser/de ---
def serialize_json(value: DaysList) -> list:
    import capo_inspector2.types.day

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.day.serialize_json(item))
    return out


def deserialize_json(data: list) -> DaysList:
    import capo_inspector2.types.day

    out: DaysList = []
    for item in data:
        out.append(capo_inspector2.types.day.deserialize_json(item))
    return out
