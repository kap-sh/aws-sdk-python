"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

ListCisScansSortBy: TypeAlias = Literal[
    "STATUS",
    "SCHEDULED_BY",
    "SCAN_START_DATE",
    "FAILED_CHECKS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATUS",
        "SCHEDULED_BY",
        "SCAN_START_DATE",
        "FAILED_CHECKS",
    )
)


def serialize_json(value: ListCisScansSortBy) -> str:
    return value


def deserialize_json(data: str) -> ListCisScansSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListCisScansSortBy value: {data!r}")
    return cast(ListCisScansSortBy, data)
