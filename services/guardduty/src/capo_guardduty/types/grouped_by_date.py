"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByDate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.date_statistics

GroupedByDate: TypeAlias = list["capo_guardduty.types.date_statistics.DateStatistics"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByDate) -> list:
    import capo_guardduty.types.date_statistics

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.date_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByDate:
    import capo_guardduty.types.date_statistics

    out: GroupedByDate = []
    for item in data:
        out.append(capo_guardduty.types.date_statistics.deserialize_json(item))
    return out
