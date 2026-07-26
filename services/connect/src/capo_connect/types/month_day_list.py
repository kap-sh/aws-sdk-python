"""Generated from Smithy shape ``com.amazonaws.connect#MonthDayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.month_day

MonthDayList: TypeAlias = list["capo_connect.types.month_day.MonthDay"]


# --- restJson1 ser/de ---
def serialize_json(value: MonthDayList) -> list:
    return list(value)


def deserialize_json(data: list) -> MonthDayList:
    return list(data)
