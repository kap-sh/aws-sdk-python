"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_column_name

AnalysisRuleColumnList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_rule_column_name.AnalysisRuleColumnName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleColumnList) -> list:
    return list(value)


def deserialize_json(data: list) -> AnalysisRuleColumnList:
    return list(data)
