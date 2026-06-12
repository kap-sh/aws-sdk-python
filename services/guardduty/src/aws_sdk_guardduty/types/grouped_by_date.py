"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByDate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.date_statistics

GroupedByDate: TypeAlias = list[
    "aws_sdk_guardduty.types.date_statistics.DateStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByDate) -> list:
    import aws_sdk_guardduty.types.date_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.date_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByDate:
    import aws_sdk_guardduty.types.date_statistics

    out: GroupedByDate = []
    for item in data:
        out.append(aws_sdk_guardduty.types.date_statistics.deserialize_json(item))
    return out
