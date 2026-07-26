"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByFindingType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.finding_type_statistics

GroupedByFindingType: TypeAlias = list[
    "capo_guardduty.types.finding_type_statistics.FindingTypeStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByFindingType) -> list:
    import capo_guardduty.types.finding_type_statistics

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.finding_type_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByFindingType:
    import capo_guardduty.types.finding_type_statistics

    out: GroupedByFindingType = []
    for item in data:
        out.append(capo_guardduty.types.finding_type_statistics.deserialize_json(item))
    return out
