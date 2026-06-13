"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportGenerationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

"""<p>Error codes for failed report generation.</p>"""
ReportGenerationErrorCode: TypeAlias = Literal[
    "INSUFFICIENT_PERMISSIONS",
    "CONFIGURATION_ERROR",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSUFFICIENT_PERMISSIONS",
        "CONFIGURATION_ERROR",
        "INTERNAL_ERROR",
    )
)


def serialize_json(value: ReportGenerationErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ReportGenerationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportGenerationErrorCode value: {data!r}")
    return cast(ReportGenerationErrorCode, data)
