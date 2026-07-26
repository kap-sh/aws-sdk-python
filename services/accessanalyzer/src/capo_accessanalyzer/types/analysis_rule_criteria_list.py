"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalysisRuleCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analysis_rule_criteria

AnalysisRuleCriteriaList: TypeAlias = list[
    "capo_accessanalyzer.types.analysis_rule_criteria.AnalysisRuleCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleCriteriaList) -> list:
    import capo_accessanalyzer.types.analysis_rule_criteria

    out: list = []
    for item in value:
        out.append(
            capo_accessanalyzer.types.analysis_rule_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalysisRuleCriteriaList:
    import capo_accessanalyzer.types.analysis_rule_criteria

    out: AnalysisRuleCriteriaList = []
    for item in data:
        out.append(
            capo_accessanalyzer.types.analysis_rule_criteria.deserialize_json(item)
        )
    return out
