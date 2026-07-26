"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DayOfWeekList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.day_of_week

DayOfWeekList: TypeAlias = list[
    "capo_workspaces_thin_client.types.day_of_week.DayOfWeek"
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfWeekList) -> list:
    import capo_workspaces_thin_client.types.day_of_week

    out: list = []
    for item in value:
        out.append(capo_workspaces_thin_client.types.day_of_week.serialize_json(item))
    return out


def deserialize_json(data: list) -> DayOfWeekList:
    import capo_workspaces_thin_client.types.day_of_week

    out: DayOfWeekList = []
    for item in data:
        out.append(capo_workspaces_thin_client.types.day_of_week.deserialize_json(item))
    return out
