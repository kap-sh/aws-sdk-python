"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportGenerationErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Error codes for failed report generation.</p>"""
ReportGenerationErrorCode: TypeAlias = Literal[
    "INSUFFICIENT_PERMISSIONS",
    "CONFIGURATION_ERROR",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportGenerationErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ReportGenerationErrorCode:
    return cast(ReportGenerationErrorCode, data)
