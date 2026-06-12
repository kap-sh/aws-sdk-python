"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatisticsTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_statistics_type

CoverageStatisticsTypeList: TypeAlias = list[
    "aws_sdk_guardduty.types.coverage_statistics_type.CoverageStatisticsType"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStatisticsTypeList) -> list:
    import aws_sdk_guardduty.types.coverage_statistics_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.coverage_statistics_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoverageStatisticsTypeList:
    import aws_sdk_guardduty.types.coverage_statistics_type

    out: CoverageStatisticsTypeList = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.coverage_statistics_type.deserialize_json(item)
        )
    return out
