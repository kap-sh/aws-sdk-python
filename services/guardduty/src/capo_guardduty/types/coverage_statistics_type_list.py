"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatisticsTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.coverage_statistics_type

CoverageStatisticsTypeList: TypeAlias = list[
    "capo_guardduty.types.coverage_statistics_type.CoverageStatisticsType"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStatisticsTypeList) -> list:
    import capo_guardduty.types.coverage_statistics_type

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.coverage_statistics_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoverageStatisticsTypeList:
    import capo_guardduty.types.coverage_statistics_type

    out: CoverageStatisticsTypeList = []
    for item in data:
        out.append(capo_guardduty.types.coverage_statistics_type.deserialize_json(item))
    return out
