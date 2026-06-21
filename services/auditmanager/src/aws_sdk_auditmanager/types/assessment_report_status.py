"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportStatus``."""

from typing import Literal, TypeAlias, cast

AssessmentReportStatus: TypeAlias = Literal[
    "COMPLETE",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentReportStatus:
    return cast(AssessmentReportStatus, data)
