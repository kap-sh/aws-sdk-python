"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationType``."""

from typing import Literal, TypeAlias, cast

AnalysisTemplateValidationType: TypeAlias = Literal["DIFFERENTIAL_PRIVACY",]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisTemplateValidationType:
    return cast(AnalysisTemplateValidationType, data)
