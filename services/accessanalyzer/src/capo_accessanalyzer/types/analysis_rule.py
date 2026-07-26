"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalysisRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analysis_rule_criteria_list


class AnalysisRule(TypedDict, closed=True):
    exclusions: NotRequired[
        "capo_accessanalyzer.types.analysis_rule_criteria_list.AnalysisRuleCriteriaList"
    ]
    """<p>A list of rules for the analyzer containing criteria to exclude from analysis. Entities that meet the rule criteria will not generate findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRule) -> dict:
    out: dict = {}
    if "exclusions" in value:
        import capo_accessanalyzer.types.analysis_rule_criteria_list

        out["exclusions"] = (
            capo_accessanalyzer.types.analysis_rule_criteria_list.serialize_json(
                value["exclusions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRule:
    out: AnalysisRule = {}  # type: ignore[typeddict-item]
    if "exclusions" in data:
        import capo_accessanalyzer.types.analysis_rule_criteria_list

        out["exclusions"] = (
            capo_accessanalyzer.types.analysis_rule_criteria_list.deserialize_json(
                data["exclusions"]
            )
        )
    return out
