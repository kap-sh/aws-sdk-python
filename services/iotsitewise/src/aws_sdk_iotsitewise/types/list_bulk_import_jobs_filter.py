"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListBulkImportJobsFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ListBulkImportJobsFilter: TypeAlias = Literal[
    "ALL",
    "PENDING",
    "RUNNING",
    "CANCELLED",
    "FAILED",
    "COMPLETED_WITH_FAILURES",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "PENDING",
        "RUNNING",
        "CANCELLED",
        "FAILED",
        "COMPLETED_WITH_FAILURES",
        "COMPLETED",
    )
)


def serialize_json(value: ListBulkImportJobsFilter) -> str:
    return value


def deserialize_json(data: str) -> ListBulkImportJobsFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListBulkImportJobsFilter value: {data!r}")
    return cast(ListBulkImportJobsFilter, data)
