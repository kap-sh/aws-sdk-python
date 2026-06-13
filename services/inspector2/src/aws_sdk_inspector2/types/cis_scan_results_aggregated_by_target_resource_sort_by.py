"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultsAggregatedByTargetResourceSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisScanResultsAggregatedByTargetResourceSortBy: TypeAlias = Literal[
    "RESOURCE_ID",
    "FAILED_COUNTS",
    "ACCOUNT_ID",
    "PLATFORM",
    "TARGET_STATUS",
    "TARGET_STATUS_REASON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_ID",
        "FAILED_COUNTS",
        "ACCOUNT_ID",
        "PLATFORM",
        "TARGET_STATUS",
        "TARGET_STATUS_REASON",
    )
)


def serialize_json(value: CisScanResultsAggregatedByTargetResourceSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanResultsAggregatedByTargetResourceSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CisScanResultsAggregatedByTargetResourceSortBy value: {data!r}"
        )
    return cast(CisScanResultsAggregatedByTargetResourceSortBy, data)
