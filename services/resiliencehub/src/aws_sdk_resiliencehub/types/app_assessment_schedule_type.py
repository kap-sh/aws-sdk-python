"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessmentScheduleType``."""

from typing import Literal, TypeAlias, cast

AppAssessmentScheduleType: TypeAlias = Literal[
    "Disabled",
    "Daily",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppAssessmentScheduleType) -> str:
    return value


def deserialize_json(data: str) -> AppAssessmentScheduleType:
    return cast(AppAssessmentScheduleType, data)
