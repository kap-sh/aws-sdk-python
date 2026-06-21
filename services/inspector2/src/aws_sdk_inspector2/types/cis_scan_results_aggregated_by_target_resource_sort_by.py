"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultsAggregatedByTargetResourceSortBy``."""

from typing import Literal, TypeAlias, cast

CisScanResultsAggregatedByTargetResourceSortBy: TypeAlias = Literal[
    "RESOURCE_ID",
    "FAILED_COUNTS",
    "ACCOUNT_ID",
    "PLATFORM",
    "TARGET_STATUS",
    "TARGET_STATUS_REASON",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultsAggregatedByTargetResourceSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanResultsAggregatedByTargetResourceSortBy:
    return cast(CisScanResultsAggregatedByTargetResourceSortBy, data)
