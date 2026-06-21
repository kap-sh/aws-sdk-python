"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleType``."""

from typing import Literal, TypeAlias, cast

AnalysisRuleType: TypeAlias = Literal[
    "AGGREGATION",
    "LIST",
    "CUSTOM",
    "ID_MAPPING_TABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisRuleType:
    return cast(AnalysisRuleType, data)
