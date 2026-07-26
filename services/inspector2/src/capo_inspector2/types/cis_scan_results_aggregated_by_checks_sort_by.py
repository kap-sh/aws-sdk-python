"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultsAggregatedByChecksSortBy``."""

from typing import Literal, TypeAlias, cast

CisScanResultsAggregatedByChecksSortBy: TypeAlias = Literal[
    "CHECK_ID",
    "TITLE",
    "PLATFORM",
    "FAILED_COUNTS",
    "SECURITY_LEVEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultsAggregatedByChecksSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanResultsAggregatedByChecksSortBy:
    return cast(CisScanResultsAggregatedByChecksSortBy, data)
