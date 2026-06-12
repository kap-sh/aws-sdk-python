"""Generated from Smithy shape ``com.amazonaws.arczonalshift#BlockedDates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.blocked_date

BlockedDates: TypeAlias = list["aws_sdk_arc_zonal_shift.types.blocked_date.BlockedDate"]


# --- restJson1 ser/de ---
def serialize_json(value: BlockedDates) -> list:
    return list(value)


def deserialize_json(data: list) -> BlockedDates:
    return list(data)
