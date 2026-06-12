"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUsageStatisticsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.usage_statistics_filter

__listOfUsageStatisticsFilter: TypeAlias = list[
    "aws_sdk_macie2.types.usage_statistics_filter.UsageStatisticsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUsageStatisticsFilter) -> list:
    import aws_sdk_macie2.types.usage_statistics_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.usage_statistics_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUsageStatisticsFilter:
    import aws_sdk_macie2.types.usage_statistics_filter

    out: __listOfUsageStatisticsFilter = []
    for item in data:
        out.append(aws_sdk_macie2.types.usage_statistics_filter.deserialize_json(item))
    return out
