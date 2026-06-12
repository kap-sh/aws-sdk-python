"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DayOfWeekList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.day_of_week

DayOfWeekList: TypeAlias = list[
    "aws_sdk_workspaces_thin_client.types.day_of_week.DayOfWeek"
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfWeekList) -> list:
    import aws_sdk_workspaces_thin_client.types.day_of_week

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_thin_client.types.day_of_week.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DayOfWeekList:
    import aws_sdk_workspaces_thin_client.types.day_of_week

    out: DayOfWeekList = []
    for item in data:
        out.append(
            aws_sdk_workspaces_thin_client.types.day_of_week.deserialize_json(item)
        )
    return out
