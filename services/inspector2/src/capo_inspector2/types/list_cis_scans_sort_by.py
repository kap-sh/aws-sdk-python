"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansSortBy``."""

from typing import Literal, TypeAlias, cast

ListCisScansSortBy: TypeAlias = Literal[
    "STATUS",
    "SCHEDULED_BY",
    "SCAN_START_DATE",
    "FAILED_CHECKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScansSortBy) -> str:
    return value


def deserialize_json(data: str) -> ListCisScansSortBy:
    return cast(ListCisScansSortBy, data)
