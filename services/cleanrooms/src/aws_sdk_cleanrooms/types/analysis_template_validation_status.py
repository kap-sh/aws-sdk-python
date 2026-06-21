"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatus``."""

from typing import Literal, TypeAlias, cast

AnalysisTemplateValidationStatus: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "UNABLE_TO_VALIDATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> AnalysisTemplateValidationStatus:
    return cast(AnalysisTemplateValidationStatus, data)
