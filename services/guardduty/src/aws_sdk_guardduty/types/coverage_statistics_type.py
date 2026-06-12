"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatisticsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

CoverageStatisticsType: TypeAlias = Literal[
    "COUNT_BY_RESOURCE_TYPE",
    "COUNT_BY_COVERAGE_STATUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COUNT_BY_RESOURCE_TYPE",
        "COUNT_BY_COVERAGE_STATUS",
    )
)


def serialize_json(value: CoverageStatisticsType) -> str:
    return value


def deserialize_json(data: str) -> CoverageStatisticsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CoverageStatisticsType value: {data!r}")
    return cast(CoverageStatisticsType, data)
