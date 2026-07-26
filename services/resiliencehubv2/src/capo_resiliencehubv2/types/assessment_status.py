"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentStatus``."""

from typing import Literal, TypeAlias, cast

AssessmentStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStatus:
    return cast(AssessmentStatus, data)
