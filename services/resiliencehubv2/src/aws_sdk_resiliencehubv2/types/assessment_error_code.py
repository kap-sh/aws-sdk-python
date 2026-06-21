"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentErrorCode``."""

from typing import Literal, TypeAlias, cast

AssessmentErrorCode: TypeAlias = Literal[
    "INVALID_PERMISSIONS",
    "CMK_ACCESS_DENIED",
    "AGENT_ERROR",
    "INTERNAL_ERROR",
    "DESIGN_FILE_ACCESS_DENIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentErrorCode) -> str:
    return value


def deserialize_json(data: str) -> AssessmentErrorCode:
    return cast(AssessmentErrorCode, data)
