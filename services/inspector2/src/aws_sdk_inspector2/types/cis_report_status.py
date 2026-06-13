"""Generated from Smithy shape ``com.amazonaws.inspector2#CisReportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisReportStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "IN_PROGRESS",
    )
)


def serialize_json(value: CisReportStatus) -> str:
    return value


def deserialize_json(data: str) -> CisReportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisReportStatus value: {data!r}")
    return cast(CisReportStatus, data)
