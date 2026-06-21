"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatisticsType``."""

from typing import Literal, TypeAlias, cast

CoverageStatisticsType: TypeAlias = Literal[
    "COUNT_BY_RESOURCE_TYPE",
    "COUNT_BY_COVERAGE_STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStatisticsType) -> str:
    return value


def deserialize_json(data: str) -> CoverageStatisticsType:
    return cast(CoverageStatisticsType, data)
