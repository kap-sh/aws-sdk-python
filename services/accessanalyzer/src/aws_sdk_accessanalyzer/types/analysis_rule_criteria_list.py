"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalysisRuleCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analysis_rule_criteria

AnalysisRuleCriteriaList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.analysis_rule_criteria.AnalysisRuleCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleCriteriaList) -> list:
    import aws_sdk_accessanalyzer.types.analysis_rule_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.analysis_rule_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalysisRuleCriteriaList:
    import aws_sdk_accessanalyzer.types.analysis_rule_criteria

    out: AnalysisRuleCriteriaList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.analysis_rule_criteria.deserialize_json(item)
        )
    return out
