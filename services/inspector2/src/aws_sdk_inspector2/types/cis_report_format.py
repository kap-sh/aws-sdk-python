"""Generated from Smithy shape ``com.amazonaws.inspector2#CisReportFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisReportFormat: TypeAlias = Literal[
    "PDF",
    "CSV",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PDF",
        "CSV",
    )
)


def serialize_json(value: CisReportFormat) -> str:
    return value


def deserialize_json(data: str) -> CisReportFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisReportFormat value: {data!r}")
    return cast(CisReportFormat, data)
