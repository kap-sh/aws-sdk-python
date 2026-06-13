"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshSchedules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.refresh_schedule

RefreshSchedules: TypeAlias = list[
    "aws_sdk_quicksight.types.refresh_schedule.RefreshSchedule"
]


# --- restJson1 ser/de ---
def serialize_json(value: RefreshSchedules) -> list:
    import aws_sdk_quicksight.types.refresh_schedule

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.refresh_schedule.serialize_json(item))
    return out


def deserialize_json(data: list) -> RefreshSchedules:
    import aws_sdk_quicksight.types.refresh_schedule

    out: RefreshSchedules = []
    for item in data:
        out.append(aws_sdk_quicksight.types.refresh_schedule.deserialize_json(item))
    return out
