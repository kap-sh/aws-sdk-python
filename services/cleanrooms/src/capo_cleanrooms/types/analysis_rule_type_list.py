"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_type

AnalysisRuleTypeList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleTypeList) -> list:
    import capo_cleanrooms.types.analysis_rule_type

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.analysis_rule_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisRuleTypeList:
    import capo_cleanrooms.types.analysis_rule_type

    out: AnalysisRuleTypeList = []
    for item in data:
        out.append(capo_cleanrooms.types.analysis_rule_type.deserialize_json(item))
    return out
