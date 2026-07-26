"""Generated from Smithy shape ``com.amazonaws.deadline#StatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.statistics

StatisticsList: TypeAlias = list["capo_deadline.types.statistics.Statistics"]


# --- restJson1 ser/de ---
def serialize_json(value: StatisticsList) -> list:
    import capo_deadline.types.statistics

    out: list = []
    for item in value:
        out.append(capo_deadline.types.statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatisticsList:
    import capo_deadline.types.statistics

    out: StatisticsList = []
    for item in data:
        out.append(capo_deadline.types.statistics.deserialize_json(item))
    return out
