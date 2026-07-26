"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListBulkImportJobsFilter``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ListBulkImportJobsFilter) -> str:
    return value


def deserialize_json(data: str) -> ListBulkImportJobsFilter:
    return cast(ListBulkImportJobsFilter, data)
