"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AllowedAnalysesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_arn_or_query_wildcard

AllowedAnalysesList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_template_arn_or_query_wildcard.AnalysisTemplateArnOrQueryWildcard"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedAnalysesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedAnalysesList:
    return list(data)
