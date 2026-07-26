"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessAnalysisRuleCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.internal_access_analysis_rule_criteria

InternalAccessAnalysisRuleCriteriaList: TypeAlias = list[
    "capo_accessanalyzer.types.internal_access_analysis_rule_criteria.InternalAccessAnalysisRuleCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessAnalysisRuleCriteriaList) -> list:
    import capo_accessanalyzer.types.internal_access_analysis_rule_criteria

    out: list = []
    for item in value:
        out.append(
            capo_accessanalyzer.types.internal_access_analysis_rule_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InternalAccessAnalysisRuleCriteriaList:
    import capo_accessanalyzer.types.internal_access_analysis_rule_criteria

    out: InternalAccessAnalysisRuleCriteriaList = []
    for item in data:
        out.append(
            capo_accessanalyzer.types.internal_access_analysis_rule_criteria.deserialize_json(
                item
            )
        )
    return out
