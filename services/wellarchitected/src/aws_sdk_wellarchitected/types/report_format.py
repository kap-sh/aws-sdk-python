"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReportFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ReportFormat: TypeAlias = Literal[
    "PDF",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PDF",
        "JSON",
    )
)


def serialize_json(value: ReportFormat) -> str:
    return value


def deserialize_json(data: str) -> ReportFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportFormat value: {data!r}")
    return cast(ReportFormat, data)
