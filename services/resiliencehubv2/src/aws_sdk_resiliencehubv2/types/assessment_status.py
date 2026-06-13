"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

AssessmentStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "PENDING",
        "IN_PROGRESS",
        "FAILED",
        "SUCCESS",
    )
)


def serialize_json(value: AssessmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentStatus value: {data!r}")
    return cast(AssessmentStatus, data)
