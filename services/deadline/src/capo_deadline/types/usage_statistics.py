"""Generated from Smithy shape ``com.amazonaws.deadline#UsageStatistics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.usage_statistic

UsageStatistics: TypeAlias = list["capo_deadline.types.usage_statistic.UsageStatistic"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatistics) -> list:
    import capo_deadline.types.usage_statistic

    out: list = []
    for item in value:
        out.append(capo_deadline.types.usage_statistic.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageStatistics:
    import capo_deadline.types.usage_statistic

    out: UsageStatistics = []
    for item in data:
        out.append(capo_deadline.types.usage_statistic.deserialize_json(item))
    return out
