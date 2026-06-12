"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByFindingType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.finding_type_statistics

GroupedByFindingType: TypeAlias = list[
    "aws_sdk_guardduty.types.finding_type_statistics.FindingTypeStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByFindingType) -> list:
    import aws_sdk_guardduty.types.finding_type_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.finding_type_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByFindingType:
    import aws_sdk_guardduty.types.finding_type_statistics

    out: GroupedByFindingType = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.finding_type_statistics.deserialize_json(item)
        )
    return out
