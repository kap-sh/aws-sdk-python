"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultsAggregatedByChecksSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisScanResultsAggregatedByChecksSortBy: TypeAlias = Literal[
    "CHECK_ID",
    "TITLE",
    "PLATFORM",
    "FAILED_COUNTS",
    "SECURITY_LEVEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHECK_ID",
        "TITLE",
        "PLATFORM",
        "FAILED_COUNTS",
        "SECURITY_LEVEL",
    )
)


def serialize_json(value: CisScanResultsAggregatedByChecksSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanResultsAggregatedByChecksSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CisScanResultsAggregatedByChecksSortBy value: {data!r}"
        )
    return cast(CisScanResultsAggregatedByChecksSortBy, data)
