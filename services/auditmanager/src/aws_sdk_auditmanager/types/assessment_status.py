"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentStatus``."""

from typing import Literal, TypeAlias, cast

AssessmentStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStatus:
    return cast(AssessmentStatus, data)
