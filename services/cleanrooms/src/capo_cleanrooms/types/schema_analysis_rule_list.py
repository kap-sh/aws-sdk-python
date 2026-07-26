"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaAnalysisRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule

SchemaAnalysisRuleList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_rule.AnalysisRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaAnalysisRuleList) -> list:
    import capo_cleanrooms.types.analysis_rule

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.analysis_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaAnalysisRuleList:
    import capo_cleanrooms.types.analysis_rule

    out: SchemaAnalysisRuleList = []
    for item in data:
        out.append(capo_cleanrooms.types.analysis_rule.deserialize_json(item))
    return out
