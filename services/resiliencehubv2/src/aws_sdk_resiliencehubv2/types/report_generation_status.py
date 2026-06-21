"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportGenerationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Status of report generation.</p>"""
ReportGenerationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> ReportGenerationStatus:
    return cast(ReportGenerationStatus, data)
