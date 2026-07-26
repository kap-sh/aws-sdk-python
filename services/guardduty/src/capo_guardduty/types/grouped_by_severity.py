"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedBySeverity``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.severity_statistics

GroupedBySeverity: TypeAlias = list[
    "capo_guardduty.types.severity_statistics.SeverityStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedBySeverity) -> list:
    import capo_guardduty.types.severity_statistics

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.severity_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedBySeverity:
    import capo_guardduty.types.severity_statistics

    out: GroupedBySeverity = []
    for item in data:
        out.append(capo_guardduty.types.severity_statistics.deserialize_json(item))
    return out
