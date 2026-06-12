"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

AssessmentReportStatus: TypeAlias = Literal[
    "COMPLETE",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: AssessmentReportStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentReportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentReportStatus value: {data!r}")
    return cast(AssessmentReportStatus, data)
