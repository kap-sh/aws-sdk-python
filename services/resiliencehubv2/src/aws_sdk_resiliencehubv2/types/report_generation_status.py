"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportGenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

"""<p>Status of report generation.</p>"""
ReportGenerationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: ReportGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> ReportGenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportGenerationStatus value: {data!r}")
    return cast(ReportGenerationStatus, data)
