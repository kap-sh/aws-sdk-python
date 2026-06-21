"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentStatus``."""

from typing import Literal, TypeAlias, cast

AssessmentStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStatus:
    return cast(AssessmentStatus, data)
